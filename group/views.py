import logging
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import resolve, reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.mixins import WriterOnlyMixin, ProjectManagerOnlyMixin
from gallery.models import Portfolio

from .models import Project, Membership, Comment, Bookmark, Apply, Share
from .forms import ProjectCreateForm, ProjectUpdateForm, MembershipUpdateForm, CommentForm

logger = logging.getLogger(__name__)


class ProjectTile(LoginRequiredMixin, ListView):
    """
    Retrieve Project List
    """
    model = Project
    context_object_name = 'project_list'
    http_method_names = ['get']
    template_name = 'group/project_list_tile.html'
    paginate_by = 9

    def get_queryset(self):
        try:
            project_list = Project.objects.all().order_by('-created_time')
        except TypeError or Project.DoesNotExist:
            project_list = []
        return project_list

    def get_context_data(self, **kwargs):
        context = super(ProjectTile, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        context['apply_list'] = Apply.objects.filter(writer=self.request.user)
        return context


class ProjectUser(LoginRequiredMixin, ListView):
    """
    Retrieve Project List
    """
    model = Project
    context_object_name = 'project_list'
    http_method_names = ['get']
    template_name = 'group/project_list_user.html'
    paginate_by = 9

    def get_queryset(self):
        project_list = Project.objects.filter(writer=self.request.user).order_by('-created_time')
        return project_list

    def get_context_data(self, **kwargs):
        context = super(ProjectUser, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        context['apply_list'] = Apply.objects.filter(writer=self.request.user)
        return context


class ProjectCreate(LoginRequiredMixin, CreateView):
    """
    Create Project
    """
    model = Project
    form_class = ProjectCreateForm
    http_method_names = ['get', 'post', ]
    template_name = 'group/project_form_create.html'

    def form_valid(self, form):
        project = form.save(commit=False)
        project.manager = self.request.user
        project.writer = self.request.user
        project.save()
        form.save_m2m()
        messages.success(self.request, _('Your project was created successfully.'))
        return super(ProjectCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(ProjectCreate, self).form_invalid(form)

    def get_success_url(self):
        # return reverse_lazy('group:project.detail', args=(self.object.id,))
        return reverse_lazy('accounts:profile.detail', args=(self.request.user.username,))


class ProjectDetail(LoginRequiredMixin, DetailView):
    """
    Detail Project
    """
    model = Project
    context_object_name = 'project'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        context['portfolio_list'] = Portfolio.objects.filter(project=self.object)
        context['membership_list'] = Membership.objects.filter(project=self.object)
        context['has_membership'] = Membership.objects.filter(project=self.object, member=self.request.user, status='A')
        context['comment_form'] = CommentForm
        return context


class ProjectUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Project
    """
    model = Project
    form_class = ProjectUpdateForm
    context_object_name = 'project'
    http_method_names = ['get', 'post', ]
    template_name = 'group/project_form_update.html'

    def form_valid(self, form):
        project = form.save(commit=False)
        project.writer = self.request.user
        project.save()
        form.save_m2m()
        messages.success(self.request, _('Your project was updated successfully.'))
        return super(ProjectUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your project was not updated!'))
        return super(ProjectUpdate, self).form_invalid(form)


class ProjectDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Project
    """
    model = Project
    context_object_name = 'project'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('group:project.user')


def project_toggle_bookmark(request, **kwargs):
    context = {}
    project = Project.objects.get(pk=kwargs["pk"])
    writer = User.objects.get(pk=request.user.pk)
    try:
        bookmark = Bookmark.objects.get(project=project, writer=writer)
        bookmark.delete()
        if project.bookmark_count > 0:
            project.bookmark_count -= 1
            project.save()
        context['class'] = 'fa fa-bookmark-o'
    except Bookmark.DoesNotExist:
        bookmark = Bookmark(project=project, writer=writer)
        bookmark.save()
        project.bookmark_count += 1
        project.save()
        context['class'] = 'fa fa-bookmark'
    context['count'] = project.bookmark_count
    context['span'] = ''.join(['#', 'badge-bookmark-', str(project.pk)])
    return JsonResponse(context)


def project_toggle_apply(request, **kwargs):
    context = {}
    project = Project.objects.get(pk=kwargs["pk"])
    writer = User.objects.get(pk=request.user.pk)
    try:
        apply = Apply.objects.get(project=project, writer=writer)
        membership = Membership.objects.get(project=project, member=writer)
        membership.delete()
        apply.delete()
        if project.apply_count > 0:
            project.apply_count -= 1
            project.save()
        context['class'] = 'fa fa-flag-o'
    except Apply.DoesNotExist:
        apply = Apply(project=project, writer=writer)
        membership = Membership(project=project, member=writer)
        membership.save()
        apply.save()
        project.apply_count += 1
        project.save()
        context['class'] = 'fa fa-flag'
    context['count'] = project.apply_count
    context['span'] = ''.join(['#', 'badge-apply-', str(project.pk)])
    return JsonResponse(context)


def project_toggle_share(request, **kwargs):
    context = {}
    project = Project.objects.get(pk=kwargs["pk"])
    writer = User.objects.get(pk=request.user.pk)
    try:
        share = Share.objects.get(project=project, writer=writer)
        share.delete()
        if project.share_count > 0:
            project.share_count -= 1
            project.save()
        context['class'] = 'fa fa-share-square-o'
    except Share.DoesNotExist:
        share = Share(project=project, writer=writer)
        share.save()
        project.share_count += 1
        project.save()
        context['class'] = 'fa fa-share-square'
    context['count'] = project.share_count
    context['span'] = ''.join(['#', 'badge-share-', str(project.pk)])
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
    template_name = 'group/membership_list_user.html'
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


class MembershipUpdate(ProjectManagerOnlyMixin, UpdateView):
    """
    Update Membership
    """
    model = Membership
    form_class = MembershipUpdateForm
    context_object_name = 'membership'
    http_method_names = ['get', 'post', ]
    template_name = 'group/membership_form_update.html'

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
    success_url = reverse_lazy('group:membership.list')


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
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        context['project'] = project
        return context


class CommentCreate(LoginRequiredMixin, CreateView):
    """
    Create Comment
    """
    model = Comment
    form_class = CommentForm
    http_method_names = ['get', 'post', ]
    template_name = 'group/comment_form.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        comment.writer = self.request.user
        comment.save()
        messages.success(self.request, _('Your comment was created successfully.'))
        return super(CommentCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(CommentCreate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        context['project'] = project
        return context


class CommentDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Comment
    """
    model = Comment
    http_method_names = ['get', 'post']

    def get_success_url(self):
        return reverse_lazy('group:project.detail', args=(self.object.project.id,))

    def delete(self, request, *args, **kwargs):
        messages.success(request, _('Your comment was deleted successfully.'))
        return super(CommentDelete, self).delete(request, *args, **kwargs)

