import logging
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import resolve, reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.mixins import WriterOnlyMixin

from accounts.models import Friend

from .models import Work, Comment, Bookmark, Apply, Share
from .forms import WorkCreateForm, WorkUpdateForm, CommentForm


logger = logging.getLogger(__name__)


def index(request):
    return redirect('job:work.tile')


class WorkTile(LoginRequiredMixin, ListView):
    """
    Retrieve Work List
    """
    model = Work
    context_object_name = 'work_list'
    http_method_names = ['get']
    template_name = 'job/work_list_tile.html'
    paginate_by = 9

    def get_queryset(self):
        work_list = Work.objects.all().order_by('-created_time')
        return work_list

    def get_context_data(self, **kwargs):
        context = super(WorkTile, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())

        return context


class WorkUser(LoginRequiredMixin, ListView):
    """
    Retrieve Work List
    """
    model = Work
    context_object_name = 'work_list'
    http_method_names = ['get']
    template_name = 'job/work_list_user.html'
    paginate_by = 9

    def get_queryset(self):
        work_list = Work.objects.filter(writer=self.request.user).order_by('-created_time')
        return work_list

    def get_context_data(self, **kwargs):
        context = super(WorkUser, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        context['work_form'] = WorkCreateForm
        context['comment_form'] = CommentForm

        return context


class WorkCreate(LoginRequiredMixin, CreateView):
    """
    Create Work
    """
    model = Work
    form_class = WorkCreateForm
    http_method_names = ['get', 'post', ]
    template_name = 'job/work_form_create.html'
    success_url = reverse_lazy('job:work.tile')

    def form_valid(self, form):
        work = form.save(commit=False)
        work.writer = self.request.user
        work.save()
        form.save_m2m()
        messages.success(self.request, _('Your work was created successfully.'))
        return super(WorkCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(WorkCreate, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('accounts:profile.detail', args=(self.request.user.username,))


class WorkDetail(LoginRequiredMixin, DetailView):
    """
    Detail Work
    """
    model = Work
    context_object_name = 'work'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(WorkDetail, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        return context


class WorkUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Work
    """
    model = Work
    form_class = WorkUpdateForm
    context_object_name = 'work'
    http_method_names = ['get', 'post', ]
    template_name = 'job/work_form_update.html'

    def form_valid(self, form):
        work = form.save(commit=False)
        work.writer = self.request.user
        work.save()
        form.save_m2m()
        messages.success(self.request, _('Your work was updated successfully.'))
        return super(WorkUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your work was not updated!'))
        return super(WorkUpdate, self).form_invalid(form)


class WorkDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Work
    """
    model = Work
    context_object_name = 'work'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('job:work.tile')


def work_toggle_friend(request, **kwargs):
    context = {}
    request_user = User.objects.get(pk=request.user.pk)
    work = Work.objects.get(pk=kwargs["pk"])
    try:
        friend = Friend.objects.get(writer=request_user, friend=work.writer)
        friend.delete()
        context['class'] = 'fa fa-chain-broken'
    except Friend.DoesNotExist:
        friend = Friend(writer=request_user, friend=work.writer)
        friend.save()
        context['class'] = 'fa fa-link'
    return JsonResponse(context)


def work_toggle_bookmark(request, **kwargs):
    context = {}
    work = Work.objects.get(pk=kwargs["pk"])
    writer = User.objects.get(pk=request.user.pk)
    try:
        bookmark = Bookmark.objects.get(work=work, writer=writer)
        bookmark.delete()
        if work.bookmark_count > 0:
            work.bookmark_count -= 1
            work.save()
        context['class'] = 'fa fa-bookmark-o'
    except Bookmark.DoesNotExist:
        bookmark = Bookmark(work=work, writer=writer)
        bookmark.save()
        work.bookmark_count += 1
        work.save()
        context['class'] = 'fa fa-bookmark'
    context['count'] = work.bookmark_count
    context['span'] = ''.join(['#', 'badge-bookmark-', str(work.pk)])
    return JsonResponse(context)


def work_toggle_apply(request, **kwargs):
    context = {}
    work = Work.objects.get(pk=kwargs["pk"])
    writer = User.objects.get(pk=request.user.pk)
    try:
        apply = Apply.objects.get(work=work, writer=writer)
        apply.delete()
        if work.apply_count > 0:
            work.apply_count -= 1
            work.save()
        context['class'] = 'fa fa-flag-o'
    except Apply.DoesNotExist:
        apply = Apply(work=work, writer=writer)
        apply.save()
        work.apply_count += 1
        work.save()
        context['class'] = 'fa fa-flag'
    context['count'] = work.apply_count
    context['span'] = ''.join(['#', 'badge-apply-', str(work.pk)])
    return JsonResponse(context)


def work_toggle_share(request, **kwargs):
    context = {}
    work = Work.objects.get(pk=kwargs["pk"])
    writer = User.objects.get(pk=request.user.pk)
    try:
        share = Share.objects.get(work=work, writer=writer)
        share.delete()
        if work.share_count > 0:
            work.share_count -= 1
            work.save()
        context['class'] = 'fa fa-share-square-o'
    except Share.DoesNotExist:
        share = Share(work=work, writer=writer)
        share.save()
        work.share_count += 1
        work.save()
        context['class'] = 'fa fa-share-square'
    context['count'] = work.share_count
    context['span'] = ''.join(['#', 'badge-share-', str(work.pk)])
    return JsonResponse(context)


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
        work = get_object_or_404(Work, pk=self.kwargs.get('pk'))
        context['work'] = work
        return context


class CommentCreate(LoginRequiredMixin, CreateView):
    """
    Create Comment
    """
    model = Comment
    form_class = CommentForm
    http_method_names = ['get', 'post', ]
    template_name = 'job/comment_form.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.work = get_object_or_404(Work, pk=self.kwargs.get('pk'))
        comment.writer = self.request.user
        comment.save()
        messages.success(self.request, _('Your comment was created successfully.'))
        return super(CommentCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(CommentCreate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        work = get_object_or_404(Work, pk=self.kwargs.get('pk'))
        context['work'] = work
        return context


class CommentDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Comment
    """
    model = Comment
    http_method_names = ['get', 'post']

    def get_success_url(self):
        return reverse_lazy('job:work.detail', args=(self.object.work.id,))

    def delete(self, request, *args, **kwargs):
        messages.success(request, _('Your comment was deleted successfully.'))
        return super(CommentDelete, self).delete(request, *args, **kwargs)

