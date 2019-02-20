import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import resolve, reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from core.mixins import WriterOnlyMixin


from .forms import PostForm, CommentForm
from .models import Section, Post, Comment

logger = logging.getLogger(__name__)


def index(request):
    return redirect('blog:post.list')


class PostList(LoginRequiredMixin, ListView):
    """
    Retrieve Post List
    """
    model = Post
    context_object_name = 'post_list'
    http_method_names = ['get']
    paginate_by = 9

    list_type = None

    def get_queryset(self):
        section = get_object_or_404(Section, name=self.kwargs['section'])
        post_list = Post.objects.filter(section=section).order_by('-created_time')
        return post_list

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['title'] = _(self.request.path.split("/")[2].capitalize())
        context['section'] = self.request.path.split("/")[2]
        context['post_form'] = PostForm
        context['comment_form'] = CommentForm

        return context


class PostCreate(LoginRequiredMixin, CreateView):
    """
    Create Post
    """
    model = Post
    form_class = PostForm
    http_method_names = ['get', 'post', ]
    template_name = 'blog/post_form_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.section = get_object_or_404(Section, name=self.kwargs['section'])
        post.writer = self.request.user
        post.save()
        messages.success(self.request, _('Your post was created successfully.'))
        return super(PostCreate, self).form_valid(form)

    def form_invalid(self, form):
        print("PostCreate-form_invalid.")
        return super(PostCreate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context['title'] = _(self.request.path.split("/")[2].capitalize())
        context['section'] = self.request.path.split("/")[2]

        return context

    def get_success_url(self):
        return reverse_lazy('blog:post.list', kwargs={'section': self.object.section.name})


class PostDetail(LoginRequiredMixin, DetailView):
    """
    Detail Post
    """
    model = Post
    context_object_name = 'post'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['title'] = _(self.request.path.split("/")[2].capitalize())
        context['section'] = self.request.path.split("/")[2]
        context['comment_form'] = CommentForm

        return context


class PostUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Post
    """
    model = Post
    form_class = PostForm
    http_method_names = ['get', 'post', ]
    template_name = 'blog/post_form_update.html'

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        post.published_date = timezone.now()
        post.save()
        messages.success(request, _('The post "{}" was updated successfully.'.format(post.title)))
        return super(PostUpdate, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data(**kwargs)
        context['title'] = _(self.request.path.split("/")[2].capitalize())
        context['section'] = self.request.path.split("/")[2]

        return context


class PostDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Post
    """
    model = Post
    http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        context = super(PostDelete, self).get_context_data(**kwargs)
        context['title'] = _(self.request.path.split("/")[2].capitalize())
        context['section'] = self.request.path.split("/")[2]

        return context

    def get_success_url(self):
        return reverse_lazy('blog:post.list', kwargs={'section': self.object.section.name})


class CommentCreate(LoginRequiredMixin, CreateView):
    """
    Create Comment
    """
    model = Comment
    form_class = CommentForm
    http_method_names = ['get', 'post', ]

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.section = get_object_or_404(Section, name=self.kwargs['section'])
        comment.post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        comment.writer = self.request.user
        comment.save()
        messages.success(self.request, _('Your comment was created successfully.'))
        return super(CommentCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(CommentCreate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        context['post'] = post
        context['title'] = _(self.request.path.split("/")[2].capitalize())
        context['section'] = self.request.path.split("/")[2]

        return context


class CommentDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Comment
    """
    model = Comment
    http_method_names = ['get', 'post']

    def delete(self, request, *args, **kwargs):
        messages.success(request, _('Your comment was deleted successfully.'))
        return super(CommentDelete, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CommentDelete, self).get_context_data(**kwargs)
        context['title'] = _(self.request.path.split("/")[2].capitalize())
        context['section'] = self.request.path.split("/")[2]

        return context

    def get_success_url(self):
        return reverse_lazy('blog:post.detail', kwargs={'section': self.request.path.split("/")[2],
                                                        'pk': self.object.post.id})

