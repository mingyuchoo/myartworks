import logging
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import resolve, reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from haystack.generic_views import SearchView

from core.mixins import WriterOnlyMixin
from accounts.models import Friend

from group.models import Project
from organization.models import Team
from job.models import Work

from .models import Portfolio, Comment, Like, Share, Report
from .forms import PortfolioCreateForm, PortfolioUpdateForm, CommentForm

logger = logging.getLogger(__name__)


def index(request):
    return redirect('gallery:portfolio.tile')


class PortfolioTile(LoginRequiredMixin, ListView):
    """
    Retrieve Portfolio Tile
    """
    model = Portfolio
    context_object_name = 'portfolio_list'
    http_method_names = ['get']
    template_name = 'gallery/portfolio_list_tile.html'
    paginate_by = 9

    def get_queryset(self):
        try:
            portfolio_list = Portfolio.objects.all().order_by('-created_time')
        except TypeError:
            portfolio_list = []
        return portfolio_list

    def get_context_data(self, **kwargs):
        context = super(PortfolioTile, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class PortfolioUser(LoginRequiredMixin, ListView):
    """
    Retrieve Portfolio List
    """
    model = Portfolio
    context_object_name = 'portfolio_list'
    http_method_names = ['get']
    template_name = 'gallery/portfolio_list_user.html'
    paginate_by = 9

    def get_queryset(self):
        portfolio_list = Portfolio.objects.filter(writer=self.request.user).order_by('-created_time')
        return portfolio_list

    def get_context_data(self, **kwargs):
        context = super(PortfolioUser, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        context['portfolio_form'] = PortfolioCreateForm
        context['comment_form'] = CommentForm

        return context


class PortfolioCreate(LoginRequiredMixin, CreateView):
    """
    Create Portfolio
    """
    model = Portfolio
    form_class = PortfolioCreateForm
    http_method_names = ['get', 'post', ]
    template_name = 'gallery/portfolio_form_create.html'
    success_url = reverse_lazy('gallery:portfolio.tile')

    def form_valid(self, form):
        writer = self.request.user
        portfolio = form.save(commit=False)
        portfolio.writer = writer
        portfolio.save()
        form.save_m2m()
        messages.success(self.request, _('Your portfolio was created successfully.'))
        return super(PortfolioCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(PortfolioCreate, self).form_invalid(form)


class PortfolioCreateForProject(LoginRequiredMixin, CreateView):
    """
    Create Portfolio for Project
    """
    model = Portfolio
    form_class = PortfolioCreateForm
    http_method_names = ['get', 'post', ]
    template_name = 'gallery/portfolio_form_create_for_project.html'
    success_url = reverse_lazy('gallery:portfolio.tile')

    def form_valid(self, form):
        writer = self.request.user
        project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        portfolio = form.save(commit=False)
        portfolio.writer = writer
        portfolio.project = project
        portfolio.save()
        form.save_m2m()
        messages.success(self.request, _('Your portfolio was created successfully.'))
        return super(PortfolioCreateForProject, self).form_valid(form)

    def form_invalid(self, form):
        return super(PortfolioCreateForProject, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(PortfolioCreateForProject, self).get_context_data(**kwargs)
        project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        context['project'] = project
        return context


class PortfolioCreateForTeam(LoginRequiredMixin, CreateView):
    """
    Create Portfolio for Project
    """
    model = Portfolio
    form_class = PortfolioCreateForm
    http_method_names = ['get', 'post', ]
    template_name = 'gallery/portfolio_form_create_for_team.html'
    success_url = reverse_lazy('gallery:portfolio.tile')

    def form_valid(self, form):
        team = get_object_or_404(Team, pk=self.kwargs.get('team_pk'))
        writer = self.request.user
        portfolio = form.save(commit=False)
        portfolio.writer = writer
        portfolio.team = team
        portfolio.save()
        form.save_m2m()
        messages.success(self.request, _('Your portfolio was created successfully.'))
        return super(PortfolioCreateForTeam, self).form_valid(form)

    def form_invalid(self, form):
        return super(PortfolioCreateForTeam, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(PortfolioCreateForTeam, self).get_context_data(**kwargs)
        team = get_object_or_404(Team, pk=self.kwargs.get('team_pk'))
        context['team'] = team
        return context


class PortfolioCreateForWork(LoginRequiredMixin, CreateView):
    """
    Create Portfolio for Project
    """
    model = Portfolio
    form_class = PortfolioCreateForm
    http_method_names = ['get', 'post', ]
    template_name = 'gallery/portfolio_form_create_for_work.html'
    success_url = reverse_lazy('gallery:portfolio.tile')

    def form_valid(self, form):
        work = get_object_or_404(Work, pk=self.kwargs.get('work_pk'))
        writer = self.request.user
        portfolio = form.save(commit=False)
        portfolio.writer = writer
        portfolio.work = work
        portfolio.save()
        form.save_m2m()
        messages.success(self.request, _('Your portfolio was created successfully.'))
        return super(PortfolioCreateForWork, self).form_valid(form)

    def form_invalid(self, form):
        return super(PortfolioCreateForWork, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(PortfolioCreateForWork, self).get_context_data(**kwargs)
        work = get_object_or_404(Work, pk=self.kwargs.get('work_pk'))
        context['work'] = work
        return context


class PortfolioDetail(LoginRequiredMixin, DetailView):
    """
    Detail Portfolio
    """
    model = Portfolio
    context_object_name = 'portfolio'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetail, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        return context


class PortfolioUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Portfolio
    """
    model = Portfolio
    form_class = PortfolioUpdateForm
    context_object_name = 'portfolio'
    http_method_names = ['get', 'post', ]
    template_name = 'gallery/portfolio_form_update.html'

    def form_valid(self, form):
        portfolio = form.save(commit=False)
        portfolio.writer = self.request.user
        portfolio.save()
        form.save_m2m()
        messages.success(self.request, _('Your portfolio was updated successfully.'))
        return super(PortfolioUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your portfolio was not updated!'))
        return super(PortfolioUpdate, self).form_invalid(form)


class PortfolioDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Portfolio
    """
    model = Portfolio
    context_object_name = 'portfolio'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('gallery:portfolio.tile')


def portfolio_toggle_friend(request, **kwargs):
    context = {}
    request_user = User.objects.get(pk=request.user.pk)
    portfolio = Portfolio.objects.get(pk=kwargs["pk"])
    try:
        friend = Friend.objects.get(writer=request_user, friend=portfolio.writer)
        friend.delete()
        context['class'] = 'fa fa-chain-broken'
    except Friend.DoesNotExist:
        friend = Friend(writer=request_user, friend=portfolio.writer)
        friend.save()
        context['class'] = 'fa fa-link'
    return JsonResponse(context)


def portfolio_toggle_like(request, **kwargs):
    context = {}
    portfolio = Portfolio.objects.get(pk=kwargs["pk"])
    writer = User.objects.get(pk=request.user.pk)
    try:
        like = Like.objects.get(portfolio=portfolio, writer=writer)
        like.delete()
        if portfolio.like_count > 0:
            portfolio.like_count -= 1
            portfolio.save()
        context['class'] = 'fa fa-heart-o'
    except Like.DoesNotExist:
        like = Like(portfolio=portfolio, writer=writer)
        like.save()
        portfolio.like_count += 1
        portfolio.save()
        context['class'] = 'fa fa-heart'
    context['count'] = portfolio.like_count
    context['span'] = ''.join(['#', 'badge-like-', str(portfolio.pk)])
    return JsonResponse(context)


def portfolio_toggle_share(request, **kwargs):
    context = {}
    portfolio = Portfolio.objects.get(pk=kwargs["pk"])
    writer = User.objects.get(pk=request.user.pk)
    try:
        share = Share.objects.get(portfolio=portfolio, writer=writer)
        share.delete()
        if portfolio.share_count > 0:
            portfolio.share_count -= 1
            portfolio.save()
        context['class'] = 'fa fa-share-square-o'
    except Share.DoesNotExist:
        share = Share(portfolio=portfolio, writer=writer)
        share.save()
        portfolio.share_count += 1
        portfolio.save()
        context['class'] = 'fa fa-share-square'
    context['count'] = portfolio.share_count
    context['span'] = ''.join(['#', 'badge-share-', str(portfolio.pk)])
    return JsonResponse(context)


def portfolio_report(request, **kwargs):
    context = {}
    context['portfolio'] = get_object_or_404(Portfolio, pk=kwargs['pk'])
    return render(request, 'gallery/report_confirm.html', context)


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
        portfolio = get_object_or_404(Portfolio, pk=self.kwargs.get('pk'))
        context['portfolio'] = portfolio
        return context


class CommentCreate(LoginRequiredMixin, CreateView):
    """
    Create Comment
    """
    model = Comment
    form_class = CommentForm
    http_method_names = ['get', 'post', ]

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.portfolio = get_object_or_404(Portfolio, pk=self.kwargs.get('pk'))
        comment.writer = self.request.user
        comment.save()
        messages.success(self.request, _('Your comment was created successfully.'))
        return super(CommentCreate, self).form_valid(form)

    def form_invalid(self, form):
        # context = {}
        # context['greeting'] = 'form_invalid'
        # return JsonResponse(context)
        return super(CommentCreate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        portfolio = get_object_or_404(Portfolio, pk=self.kwargs.get('pk'))
        context['portfolio'] = portfolio
        return context


class CommentDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Comment
    """
    model = Comment
    http_method_names = ['get', 'post']

    def get_success_url(self):
        return reverse_lazy('gallery:portfolio.detail', args=(self.object.portfolio.id,))

    def delete(self, request, *args, **kwargs):
        messages.success(request, _('Your comment was deleted successfully.'))
        return super(CommentDelete, self).delete(request, *args, **kwargs)
