import logging
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.mixins import WriterOnlyMixin


from .models import Category, Field
from .forms import CategoryForm, FieldForm

logger = logging.getLogger(__name__)


def index(request):
    return redirect('classification:category.list')


class CategoryList(LoginRequiredMixin, ListView):
    """
    Retrieve Category List
    """
    model = Category
    context_object_name = 'category_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        category_list = Category.objects.all()
        return category_list


class CategoryCreate(LoginRequiredMixin, CreateView):
    """
    Create Category
    """
    model = Category
    form_class = CategoryForm
    http_method_names = ['get', 'post', ]
    template_name = 'classification/category_form_create.html'
    success_url = reverse_lazy('classification:category.list')

    def form_valid(self, form):
        category = form.save(commit=False)
        category.writer = self.request.user
        category.save()
        messages.success(self.request, _('Your category was created successfully.'))
        return super(CategoryCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(CategoryCreate, self).form_invalid(form)


class CategoryDetail(LoginRequiredMixin, DetailView):
    """
    Detail Category
    """
    model = Category
    context_object_name = 'category'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        return context


class CategoryUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Category
    """
    model = Category
    form_class = CategoryForm
    context_object_name = 'category'
    http_method_names = ['get', 'post', ]
    template_name = 'classification/category_form_update.html'

    def form_valid(self, form):
        category = form.save(commit=False)
        category.writer = self.request.user
        category.save()
        messages.success(self.request, _('Your category was updated successfully.'))
        return super(CategoryUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your category was not updated!'))
        return super(CategoryUpdate, self).form_invalid(form)


class CategoryDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Category
    """
    model = Category
    context_object_name = 'category'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('classification:category.list')
    # def get(self, request, *args, **kwargs):
    #     context = {}
    #     context['greeting'] = 'render_to_response'
    #     return JsonResponse(context)



class FieldList(LoginRequiredMixin, ListView):
    """
    Retrieve Field List
    """
    model = Field
    context_object_name = 'field_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        field_list = Field.objects.all()
        return field_list


class FieldCreate(LoginRequiredMixin, CreateView):
    """
    Create Field
    """
    model = Field
    form_class = FieldForm
    http_method_names = ['get', 'post', ]
    template_name = 'classification/field_form_create.html'
    success_url = reverse_lazy('classification:field.list')

    def form_valid(self, form):
        field = form.save(commit=False)
        field.writer = self.request.user
        field.save()
        messages.success(self.request, _('Your field was created successfully.'))
        return super(FieldCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(FieldCreate, self).form_invalid(form)


class FieldDetail(LoginRequiredMixin, DetailView):
    """
    Detail Field
    """
    model = Field
    context_object_name = 'field'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(FieldDetail, self).get_context_data(**kwargs)
        return context


class FieldUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Field
    """
    model = Field
    form_class = FieldForm
    context_object_name = 'field'
    http_method_names = ['get', 'post', ]
    template_name = 'classification/field_form_update.html'

    def form_valid(self, form):
        field = form.save(commit=False)
        field.writer = self.request.user
        field.save()
        messages.success(self.request, _('Your field was updated successfully.'))
        return super(FieldUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your field was not updated!'))
        return super(FieldUpdate, self).form_invalid(form)


class FieldDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Field
    """
    model = Field
    context_object_name = 'field'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('classification:field.list')
    # def get(self, request, *args, **kwargs):
    #     context = {}
    #     context['greeting'] = 'render_to_response'
    #     return JsonResponse(context)

