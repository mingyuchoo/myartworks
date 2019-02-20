import logging
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import resolve, reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Message
from .forms import MessageSendForm, MessageReplyForm

logger = logging.getLogger(__name__)


def index(request):
    context = {}
    return render(request, 'messagebox:message.list', context)


class MessageList(LoginRequiredMixin, ListView):
    """
    Retrieve Message List
    """
    model = Message
    context_object_name = 'message_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        message_list = Message.objects.filter(box='I', sender=self.request.user).order_by('-send_time')

        return message_list

    def get_context_data(self, **kwargs):
        context = super(MessageList, self).get_context_data(**kwargs)
        received_list = Message.objects.filter(box='I', receiver=self.request.user).order_by('-send_time')
        archived_list = Message.objects.filter(box='A').filter(Q(sender=self.request.user) |
                                                               Q(receiver=self.request.user)).order_by('-send_time')

        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        context['received_list'] = received_list
        context['archived_list'] = archived_list

        return context


class MessageSend(LoginRequiredMixin, CreateView):
    """
    Create Message
    """
    model = Message
    form_class = MessageSendForm
    http_method_names = ['get', 'post', ]
    template_name = 'messagebox/message_form_send.html'
    success_url = reverse_lazy('messagebox:message.list')

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.save()
        messages.success(self.request, _('Your message was created successfully.'))
        return super(MessageSend, self).form_valid(form)

    def form_invalid(self, form):
        return super(MessageSend, self).form_invalid(form)


class MessageDetail(LoginRequiredMixin, DetailView):
    """
    Detail Message
    """
    model = Message
    context_object_name = 'message'
    http_method_names = ['get']

    def get_object(self, queryset=None):
        obj = super(MessageDetail, self).get_object(queryset=None)
        if obj.receiver == self.request.user:
            obj.status = 'R'
            obj.receive_time = timezone.now()
            obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super(MessageDetail, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class MessageReply(LoginRequiredMixin, CreateView):
    """
    Update Message
    """
    model = Message
    form_class = MessageReplyForm
    context_object_name = 'message'
    http_method_names = ['get', 'post', ]
    template_name = 'messagebox/message_form_reply.html'

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.receiver = get_object_or_404(Message, pk=self.kwargs['pk']).sender
        message.save()
        messages.success(self.request, _('Your message was updated successfully.'))
        return super(MessageReply, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your message was not updated!'))
        return super(MessageReply, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(MessageReply, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        try:
            context['received_message'] = Message.objects.get(pk=self.kwargs['pk'])
        except:
            pass
        return context


class MessageArchive(LoginRequiredMixin, DeleteView):
    """
    Archive Message
    """
    model = Message
    context_object_name = 'message'
    http_method_names = ['get', 'post']
    template_name = 'messagebox/message_confirm_archive.html'
    success_url = reverse_lazy('messagebox:message.list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        if self.object.sender == request.user or self.object.receiver ==request.user:
            self.object.box = 'A'
            self.object.archive_time = timezone.now()
            self.object.save()
        return HttpResponseRedirect(success_url)


class MessageDelete(LoginRequiredMixin, DeleteView):
    """
    Delete Message
    """
    model = Message
    context_object_name = 'message'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('messagebox:message.list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        if self.object.sender == request.user or self.object.receiver == request.user:
            self.object.box = 'D'
            self.object.delete_time = timezone.now()
            self.object.save()
        return HttpResponseRedirect(success_url)
