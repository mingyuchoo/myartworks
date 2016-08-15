from django.contrib.auth import (login as auth_login,
                                 logout as auth_logout,
                                 update_session_auth_hash
                                 )
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy, resolve
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse

from django.db import transaction
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.mixins import WriterOnlyMixin

from .models import Profile, Friend, Credit
from resume.models import Basic, Contact, Letter
from .forms import UserForm, ProfileForm, ProfileSimpleForm, FriendForm

from gallery.models import (Portfolio,
                            Comment as PortfolioComment,
                            Like as PortfolioLike
                            )
from job.models import (Work,
                        Comment as WorkComment,
                        Bookmark as WorkBookmark,
                        Apply as WorkApply
                        )
from group.models import (Project,
                          Comment as ProjectComment,
                          Bookmark as ProjectBookmark,
                          Apply as ProjectApply
                          )
from organization.models import (Team,
                                 Comment as TeamComment,
                                 Bookmark as TeamBookmark,
                                 Apply as TeamApply
                                 )


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # messages.success(request, _('Nice to see you again.'))
            return HttpResponseRedirect(reverse('common:index'))
    else:
        form = AuthenticationForm(request)
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('common:index'))


@transaction.non_atomic_requests
def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileSimpleForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # save user object
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            # save profile object
            profile = profile_form.save(commit=False)
            profile.writer = user
            profile.save()

            # 1) create user's group
            category_list = ['view', 'add', 'change', 'delete']
            # category_list = ['all']
            for category in category_list:
                new_group = Group.objects.create(name=''.join([user.username, '_', category]))
                new_group.save()
                user.groups.add(new_group)
            # 2) search all content type to add
            default_contenttypes = ['admin', 'auth', 'contenttypes', 'sessions']
            permissions = Permission.objects.all()
            filtered_permissions = [permission
                                    for permission in permissions
                                    if permission.content_type.app_label not in default_contenttypes
                                    ]
            # 3) make default permissions - users groups
            for category in category_list:
                user_groups = user.groups.all()
                [group.permissions.add(permission)
                 for group in user_groups
                 for permission in filtered_permissions
                 if category in set(group.name.split('_')).intersection(set(permission.codename.split('_')))
                 ]

            # 4) create resume.basic
            basic = Basic.objects.create(writer=user)
            basic.save()
            # 5) create resume.contact
            contact = Contact.objects.create(writer=user)
            contact.save()
            # 6) create resume.letter
            letter = Letter.objects.create(writer=user)
            letter.save()

            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        user_form = UserCreationForm()
        profile_form = ProfileSimpleForm()
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'accounts/profile_form_create.html', context)


# @login_required
# def detail(request, username):
#
#     context = {}
#     user = User.objects.get(username=username)
#     profile = user.profile
#     context['profile'] = profile
#
#     portfolio_comment = PortfolioComment.objects.filter(writer=user)
#     work_comment = WorkComment.objects.filter(writer=user)
#     project_comment = ProjectComment.objects.filter(writer=user)
#     team_comment = TeamComment.objects.filter(writer=user)
#     context['portfolio_comment'] = portfolio_comment
#     context['work_comment'] = work_comment
#     context['project_comment'] = project_comment
#     context['team_comment'] = team_comment
#
#     portfolio_like = PortfolioLike.objects.filter(writer=user)
#     context['portfolio_like'] = portfolio_like
#
#     work_bookmark = WorkBookmark.objects.filter(writer=user)
#     project_bookmark = ProjectBookmark.objects.filter(writer=user)
#     team_bookmark = TeamBookmark.objects.filter(writer=user)
#     context['work_bookmark'] = work_bookmark
#     context['project_bookmark'] = project_bookmark
#     context['team_bookmark'] = team_bookmark
#
#     work_apply = WorkApply.objects.filter(writer=user)
#     project_apply = ProjectApply.objects.filter(writer=user)
#     team_apply = TeamApply.objects.filter(writer=user)
#     context['work_apply'] = work_apply
#     context['project_apply'] = project_apply
#     context['team_apply'] = team_apply
#
#     return render(request, 'accounts/profile_detail.html', context)


@login_required
def update(request):
    if request.method == 'POST' and request.user.is_authenticated():
        if 'update' in request.POST:
            user_form = UserForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user = user_form.save(commit=False)
                profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
                if profile_form.is_valid():
                    profile = profile_form.save(commit=False)
                    profile.writer = user
                    profile.picture = request.FILES.get('picture', 'profile_picture/default.png')
                    profile.save()
                    user.save()
                    context = {'user_form': user_form, 'profile_form': profile_form, 'username': request.user.username}
                    return render(request, 'accounts/profile_form_update.html', context)
                else:
                    print('profile_form is invalid')
            else:
                print('user_form is invalid')
                return HttpResponseRedirect(reverse('common:index'))
        elif 'deactivate' in request.POST:
            user_form = UserForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user = user_form.save(commit=False)
                user.is_active = False
                user.save()
                print("User is deactivated.")
                return HttpResponseRedirect(reverse('accounts:logout'))
        else:
            print("accounts.delete didn't work.")
    else:
        try:
            user_form = UserForm(instance=request.user)
            try:
                profile = request.user.profile
                profile_form = ProfileForm(instance=profile)
            except Profile.DoesNotExist:
                profile_form = ProfileForm()
        except User.DoesNotExist:
            user_form = UserForm()
    context = {'user_form': user_form, 'profile_form': profile_form, 'username': request.user.username}
    return render(request, 'accounts/profile_form_update.html', context)


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return reverse_lazy('index')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/password_change.html', {'form': form})


@login_required
def join_group(request, username):
    user = User.objects.get(username=username)
    group = user.groups.get(name=''.join([username, '_view']))
    group.user_set.add(request.user)
    return HttpResponseRedirect(reverse('common:index'))


@login_required
def groups(request, username):
    user = User.objects.get(username=username)
    groups = set([group.name.split('_')[0] for group in user.groups.exclude(name__startswith=user.username)])
    context = {'groups': groups, 'title': 'Group'}
    return render(request, 'accounts/profile_group_list.html', context)


@login_required
def search(request):
    groups = None
    if request.method == 'POST':
        keyword = request.POST['search'].strip()
        groups = set([group.name.split('_')[0] for group in Group.objects.filter(name__startswith=keyword)])
    else:
        pass
    return render(request, 'accounts/profile_group_list.html', {'groups': groups})


class FriendList(LoginRequiredMixin, ListView):
    """
    Retrieve Friend List
    """
    model = Friend
    context_object_name = 'friend_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        friend_list = Friend.objects.filter(writer__username=self.kwargs.get('username')).order_by('-created_time')
        return friend_list

    def get_context_data(self, **kwargs):
        context = super(FriendList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class FriendForList(LoginRequiredMixin, ListView):
    """
    Retrieve Friend List
    """
    model = Friend
    context_object_name = 'friend_list'
    http_method_names = ['get']
    template_name = 'accounts/friend_list_for.html'
    paginate_by = 9

    def get_queryset(self):
        friend_list = Friend.objects.filter(friend__username=self.kwargs.get('username')).order_by('-created_time')
        return friend_list

    def get_context_data(self, **kwargs):
        context = super(FriendForList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class FriendCreate(LoginRequiredMixin, CreateView):
    """
    Create Friend
    """
    model = Friend
    form_class = FriendForm
    http_method_names = ['get', 'post', ]
    success_url = reverse_lazy('accounts:friend.list')

    def form_valid(self, form):
        friend = form.save(commit=False)
        friend.writer = self.request.user
        friend.save()
        messages.success(self.request, _('Your friend was created successfully.'))
        return super(FriendCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(FriendCreate, self).form_invalid(form)


class FriendDetail(LoginRequiredMixin, DetailView):
    """
    Detail Friend
    """
    model = Friend
    context_object_name = 'friend'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(FriendDetail, self).get_context_data(**kwargs)
        return context


class FriendUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Friend
    """
    model = Friend
    form_class = FriendForm
    context_object_name = 'friend'
    http_method_names = ['get', 'post', ]

    def form_valid(self, form):
        friend = form.save(commit=False)
        friend.writer = self.request.user
        friend.save()
        messages.success(self.request, _('Your friend was updated successfully.'))
        return super(FriendUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your friend was not updated!'))
        return super(FriendUpdate, self).form_invalid(form)


class FriendDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Friend
    """
    model = Friend
    context_object_name = 'friend'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('accounts:friend.list')


class ProfileList(LoginRequiredMixin, ListView):
    """
    Retrieve Profile List
    """
    model = Profile
    context_object_name = 'profile_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        profile_list = Profile.objects.all()
        return profile_list

    def get_context_data(self, **kwargs):
        context = super(ProfileList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class ProfileDetail(LoginRequiredMixin, DetailView):
    """
    Detail Profile
    """
    model = Profile
    context_object_name = 'profile'
    http_method_names = ['get']

    slug_field = 'writer__username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        context['portfolio_list'] = Portfolio.objects.filter(writer=self.object.writer)
        context['work_list'] = Work.objects.filter(writer=self.object.writer)
        context['project_list'] = Project.objects.filter(writer=self.object.writer)
        context['team_list'] = Team.objects.filter(writer=self.object.writer)

        work_apply = WorkApply.objects.filter(writer=self.object.writer)
        project_apply = ProjectApply.objects.filter(writer=self.object.writer)
        team_apply = TeamApply.objects.filter(writer=self.object.writer)
        context['work_apply'] = work_apply
        context['project_apply'] = project_apply
        context['team_apply'] = team_apply

        work_bookmark = WorkBookmark.objects.filter(writer=self.object.writer)
        project_bookmark = ProjectBookmark.objects.filter(writer=self.object.writer)
        team_bookmark = TeamBookmark.objects.filter(writer=self.object.writer)
        context['work_bookmark'] = work_bookmark
        context['project_bookmark'] = project_bookmark
        context['team_bookmark'] = team_bookmark

        # portfolio_comment = PortfolioComment.objects.filter(writer=self.object.writer)
        # work_comment = WorkComment.objects.filter(writer=self.object.writer)
        # project_comment = ProjectComment.objects.filter(writer=self.object.writer)
        # team_comment = TeamComment.objects.filter(writer=self.object.writer)
        # context['portfolio_comment'] = portfolio_comment
        # context['work_comment'] = work_comment
        # context['project_comment'] = project_comment
        # context['team_comment'] = team_comment
        #
        # portfolio_like = PortfolioLike.objects.filter(writer=self.object.writer)
        # context['portfolio_like'] = portfolio_like


        return context


class ProfileUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Profile
    """
    model = Profile
    form_class = ProfileForm
    context_object_name = 'profile'
    http_method_names = ['get', 'post', ]
    template_name = 'accounts/profile_form_update.html'

    slug_field = 'writer__username'
    slug_url_kwarg = 'username'

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.writer = self.request.user
        profile.save()
        form.save_m2m()
        messages.success(self.request, _('Your profile was updated successfully.'))
        return super(ProfileUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your profile was not updated!'))
        return super(ProfileUpdate, self).form_invalid(form)


def profile_toggle_friend(request, **kwargs):
    context = {}
    request_user = User.objects.get(pk=request.user.pk)   # 나
    profile = Profile.objects.get(writer__username=kwargs["username"])  # 상대
    try:
        friend = Friend.objects.get(writer=request_user, friend=profile.writer)
        friend.delete()
        context['class'] = 'fa fa-chain-broken'
    except Friend.DoesNotExist:
        friend = Friend(writer=request_user, friend=profile.writer)
        friend.save()
        context['class'] = 'fa fa-link'
    return JsonResponse(context)


def profile_toggle_credit(request, **kwargs):
    context = {}
    request_user = User.objects.get(pk=request.user.pk) # 나
    profile = Profile.objects.get(writer__username=kwargs["username"])  # 상대
    try:
        credit = Credit.objects.get(profile=profile, writer=request_user)
        credit.delete()
        if profile.credit_count > 0:
            profile.credit_count -= 1
            profile.save()
        context['class'] = 'fa fa-star-o'
    except Credit.DoesNotExist:
        credit = Credit(profile=profile, writer=request_user)
        credit.save()
        profile.credit_count += 1
        profile.save()
        context['class'] = 'fa fa-star'
    context['count'] = profile.credit_count
    context['span'] = ''.join(['#', 'badge-credit-', str(profile.writer.username)])
    return JsonResponse(context)
