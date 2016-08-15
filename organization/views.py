import logging
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import resolve, reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from core.mixins import WriterOnlyMixin, TeamLeaderOnlyMixin


from .models import Team, Comment, Membership, Bookmark, Apply, Share
from .forms import TeamCreateForm, TeamUpdateForm, MembershipUpdateForm, CommentForm

logger = logging.getLogger(__name__)


class TeamTile(LoginRequiredMixin, ListView):
    """
    Retrieve Team Tile
    """
    model = Team
    context_object_name = 'team_list'
    http_method_names = ['get']
    template_name = 'organization/team_list_tile.html'
    paginate_by = 9

    def get_queryset(self):
        try:
            team_list = Team.objects.all().order_by('-created_time')
        except TypeError or Team.DoesNotExist:
            team_list = []
        return team_list

    def get_context_data(self, **kwargs):
        context = super(TeamTile, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        context['apply_list'] = Apply.objects.filter(writer=self.request.user)
        return context


class TeamUser(LoginRequiredMixin, ListView):
    """
    Retrieve Team User
    """
    model = Team
    context_object_name = 'team_list'
    http_method_names = ['get']
    template_name = 'organization/team_list_user.html'
    paginate_by = 9

    def get_queryset(self):
        team_list = Team.objects.filter(writer=self.request.user).order_by('-created_time')
        return team_list

    def get_context_data(self, **kwargs):
        context = super(TeamUser, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        context['apply_list'] = Apply.objects.filter(writer=self.request.user)
        return context


class TeamCreate(LoginRequiredMixin, CreateView):
    """
    Create Team
    """
    model = Team
    form_class = TeamCreateForm
    http_method_names = ['get', 'post', ]
    template_name = 'organization/team_form_create.html'

    def form_valid(self, form):
        team = form.save(commit=False)
        team.leader = self.request.user
        team.writer = self.request.user
        team.save()
        form.save_m2m()
        messages.success(self.request, _('Your team was created successfully.'))
        return super(TeamCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(TeamCreate, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('organization:team.detail', args=(self.object.id,))


class TeamDetail(LoginRequiredMixin, DetailView):
    """
    Detail Team
    """
    model = Team
    context_object_name = 'team'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(TeamDetail, self).get_context_data(**kwargs)
        context['membership_list'] = Membership.objects.filter(team=self.object)
        context['has_membership'] = Membership.objects.filter(team=self.object, member=self.request.user, status='A')
        context['comment_form'] = CommentForm
        return context


class TeamUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Team
    """
    model = Team
    form_class = TeamUpdateForm
    context_object_name = 'team'
    http_method_names = ['get', 'post', ]
    template_name = 'organization/team_form_update.html'

    def form_valid(self, form):
        team = form.save(commit=False)
        team.writer = self.request.user
        team.save()
        form.save_m2m()
        messages.success(self.request, _('Your team was updated successfully.'))
        return super(TeamUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your team was not updated!'))
        return super(TeamUpdate, self).form_invalid(form)


class TeamDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Team
    """
    model = Team
    context_object_name = 'team'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('organization:team.user')


def team_toggle_bookmark(request, **kwargs):
    context = {}
    team = Team.objects.get(pk=kwargs["pk"])
    writer = User.objects.get(pk=request.user.pk)
    try:
        bookmark = Bookmark.objects.get(team=team, writer=writer)
        bookmark.delete()
        if team.bookmark_count > 0:
            team.bookmark_count -= 1
            team.save()
        context['class'] = 'fa fa-bookmark-o'
    except Bookmark.DoesNotExist:
        bookmark = Bookmark(team=team, writer=writer)
        bookmark.save()
        team.bookmark_count += 1
        team.save()
        context['class'] = 'fa fa-bookmark'
    context['count'] = team.bookmark_count
    context['span'] = ''.join(['#', 'badge-bookmark-', str(team.pk)])
    return JsonResponse(context)


def team_toggle_apply(request, **kwargs):
    context = {}
    team = Team.objects.get(pk=kwargs["pk"])
    writer = User.objects.get(pk=request.user.pk)
    try:
        apply = Apply.objects.get(team=team, writer=writer)
        membership = Membership.objects.get(team=team, member=writer)
        membership.delete()
        apply.delete()
        if team.apply_count > 0:
            team.apply_count -= 1
            team.save()
        context['class'] = 'fa fa-flag-o'
    except Apply.DoesNotExist:
        apply = Apply(team=team, writer=writer)
        membership = Membership(team=team, member=writer)
        membership.save()
        apply.save()
        team.apply_count += 1
        team.save()
        context['class'] = 'fa fa-flag'
    context['count'] = team.apply_count
    context['span'] = ''.join(['#', 'badge-apply-', str(team.pk)])
    return JsonResponse(context)


def team_toggle_share(request, **kwargs):
    context = {}
    team = Team.objects.get(pk=kwargs["pk"])
    writer = User.objects.get(pk=request.user.pk)
    try:
        share = Share.objects.get(team=team, writer=writer)
        share.delete()
        if team.share_count > 0:
            team.share_count -= 1
            team.save()
        context['class'] = 'fa fa-share-square-o'
    except Share.DoesNotExist:
        share = Share(team=team, writer=writer)
        share.save()
        team.share_count += 1
        team.save()
        context['class'] = 'fa fa-share-square'
    context['count'] = team.share_count
    context['span'] = ''.join(['#', 'badge-share-', str(team.pk)])
    return JsonResponse(context)


class MembershipList(LoginRequiredMixin, ListView):
    """
    Retrieve Membership List
    """
    model = Membership
    context_object_name = 'membership_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        membership_list = Membership.objects.all()
        return membership_list

    def get_context_data(self, **kwargs):
        context = super(MembershipList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        context['membership_form'] = MembershipUpdateForm
        return context


class MembershipListUser(LoginRequiredMixin, ListView):
    """
    Retrieve Membership List
    """
    model = Membership
    context_object_name = 'membership_list'
    http_method_names = ['get']
    # template_name = 'organization/membership_list_user.html'
    paginate_by = 9

    def get_queryset(self):
        membership_list = Membership.objects.filter(member=self.request.user).order_by('requested_date')
        return membership_list

    def get_context_data(self, **kwargs):
        context = super(MembershipListUser, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class MembershipDetail(LoginRequiredMixin, DetailView):
    """
    Detail Membership
    """
    model = Membership
    context_object_name = 'membership'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(MembershipDetail, self).get_context_data(**kwargs)
        return context


class MembershipUpdate(TeamLeaderOnlyMixin, UpdateView):
    """
    Update Membership
    """
    model = Membership
    form_class = MembershipUpdateForm
    context_object_name = 'membership'
    http_method_names = ['get', 'post', ]
    template_name = 'organization/membership_form_update.html'

    def form_valid(self, form):
        membership = form.save(commit=False)
        if membership.status == 'A':
            membership.joined_date = timezone.now()
        else:
            membership.joined_date = None
        membership.save()
        messages.success(self.request, _('Your membership was updated successfully.'))
        return super(MembershipUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your membership was not updated!'))
        return super(MembershipUpdate, self).form_invalid(form)


class MembershipDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Membership
    """
    model = Membership
    context_object_name = 'membership'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('organization:membership.list')


class CommentList(LoginRequiredMixin, ListView):
    """
    Comment List
    """
    model = Comment
    context_object_name = 'comment_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        comment_list = Comment.objects.all().order_by('-created_time')
        return comment_list

    def get_context_data(self, **kwargs):
        context = super(CommentList, self).get_context_data(**kwargs)
        team = get_object_or_404(Team, pk=self.kwargs.get('pk'))
        context['team'] = team
        return context


class CommentCreate(LoginRequiredMixin, CreateView):
    """
    Create Comment
    """
    model = Comment
    form_class = CommentForm
    http_method_names = ['get', 'post', ]
    template_name = 'organization/comment_form.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.team = get_object_or_404(Team, pk=self.kwargs.get('pk'))
        comment.writer = self.request.user
        comment.save()
        messages.success(self.request, _('Your comment was created successfully.'))
        return super(CommentCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(CommentCreate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        team = get_object_or_404(Team, pk=self.kwargs.get('pk'))
        context['team'] = team
        return context


class CommentDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Comment
    """
    model = Comment
    http_method_names = ['get', 'post']

    def get_success_url(self):
        return reverse_lazy('organization:team.detail', args=(self.object.team.id,))

    def delete(self, request, *args, **kwargs):
        messages.success(request, _('Your comment was deleted successfully.'))
        return super(CommentDelete, self).delete(request, *args, **kwargs)

