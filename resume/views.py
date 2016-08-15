import logging
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import resolve, reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.mixins import WriterOnlyMixin


from .models import (Basic,
                     Contact,
                     Letter,
                     Career,
                     Education,
                     Award,
                     Certificate,
                     Language,
                     Skill)

from .forms import (BasicForm,
                    ContactForm,
                    LetterForm,
                    CareerForm,
                    EducationForm,
                    AwardForm,
                    CertificateForm,
                    LanguageForm,
                    SkillForm)


logger = logging.getLogger(__name__)


def index(request):
    context = {}

    try:
        basic = Basic.objects.get(writer=request.user)
        contact = Contact.objects.get(writer=request.user)
        letter = Letter.objects.get(writer=request.user)
        career_list = Career.objects.filter(writer=request.user)
        education_list = Education.objects.filter(writer=request.user)
        award_list = Award.objects.filter(writer=request.user)
        certificate_list = Certificate.objects.filter(writer=request.user)
        language_list = Language.objects.filter(writer=request.user)
        skill_list = Skill.objects.filter(writer=request.user)

        context['title'] = _(resolve(request.path).app_name.capitalize())
        context['basic'] = basic
        context['contact'] = contact
        context['letter'] = letter
        context['career_list'] = career_list
        context['education_list'] = education_list
        context['award_list'] = award_list
        context['certificate_list'] = certificate_list
        context['language_list'] = language_list
        context['skill_list'] = skill_list
    except TypeError:
        return redirect('accounts:login')
    return render(request, 'resume/index.html', context)


class BasicList(LoginRequiredMixin, ListView):
    """
    Retrieve Basic List
    """
    model = Basic
    context_object_name = 'basic_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        basic_list = Basic.objects.all()
        return basic_list

    def get_context_data(self, **kwargs):
        context = super(BasicList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class BasicCreate(LoginRequiredMixin, CreateView):
    """
    Create Basic
    """
    model = Basic
    form_class = BasicForm
    http_method_names = ['get', 'post', ]
    success_url = reverse_lazy('resume:index')

    def form_valid(self, form):
        basic = form.save(commit=False)
        basic.writer = self.request.user
        basic.save()
        messages.success(self.request, _('Your basic was created successfully.'))
        return super(BasicCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(BasicCreate, self).form_invalid(form)


class BasicDetail(LoginRequiredMixin, DetailView):
    """
    Detail Basic
    """
    model = Basic
    context_object_name = 'basic'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(BasicDetail, self).get_context_data(**kwargs)
        return context


class BasicUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Basic
    """
    model = Basic
    form_class = BasicForm
    context_object_name = 'basic'
    http_method_names = ['get', 'post', ]

    def form_valid(self, form):
        basic = form.save(commit=False)
        basic.writer = self.request.user
        basic.save()
        messages.success(self.request, _('Your basic was updated successfully.'))
        return super(BasicUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your basic was not updated!'))
        return super(BasicUpdate, self).form_invalid(form)


class BasicDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Basic
    """
    model = Basic
    context_object_name = 'basic'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('resume:index')


class ContactList(LoginRequiredMixin, ListView):
    """
    Retrieve Contact List
    """
    model = Contact
    context_object_name = 'contact_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        contact_list = Contact.objects.all()
        return contact_list

    def get_context_data(self, **kwargs):
        context = super(ContactList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class ContactCreate(LoginRequiredMixin, CreateView):
    """
    Create Contact
    """
    model = Contact
    form_class = ContactForm
    http_method_names = ['get', 'post', ]
    success_url = reverse_lazy('resume:index')

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.writer = self.request.user
        contact.save()
        messages.success(self.request, _('Your contact was created successfully.'))
        return super(ContactCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(ContactCreate, self).form_invalid(form)


class ContactDetail(LoginRequiredMixin, DetailView):
    """
    Detail Contact
    """
    model = Contact
    context_object_name = 'contact'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(ContactDetail, self).get_context_data(**kwargs)
        return context


class ContactUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Contact
    """
    model = Contact
    form_class = ContactForm
    context_object_name = 'contact'
    http_method_names = ['get', 'post', ]

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.writer = self.request.user
        contact.save()
        messages.success(self.request, _('Your contact was updated successfully.'))
        return super(ContactUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your contact was not updated!'))
        return super(ContactUpdate, self).form_invalid(form)


class ContactDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Contact
    """
    model = Contact
    context_object_name = 'contact'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('resume:index')


class LetterList(LoginRequiredMixin, ListView):
    """
    Retrieve Letter List
    """
    model = Letter
    context_object_name = 'letter_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        letter_list = Letter.objects.all()
        return letter_list

    def get_context_data(self, **kwargs):
        context = super(LetterList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class LetterCreate(LoginRequiredMixin, CreateView):
    """
    Create Letter
    """
    model = Letter
    form_class = LetterForm
    http_method_names = ['get', 'post', ]
    success_url = reverse_lazy('resume:index')

    def form_valid(self, form):
        letter = form.save(commit=False)
        letter.writer = self.request.user
        letter.save()
        messages.success(self.request, _('Your letter was created successfully.'))
        return super(LetterCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(LetterCreate, self).form_invalid(form)


class LetterDetail(LoginRequiredMixin, DetailView):
    """
    Detail Letter
    """
    model = Letter
    context_object_name = 'letter'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(LetterDetail, self).get_context_data(**kwargs)
        return context


class LetterUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Letter
    """
    model = Letter
    form_class = LetterForm
    context_object_name = 'letter'
    http_method_names = ['get', 'post', ]

    def form_valid(self, form):
        letter = form.save(commit=False)
        letter.writer = self.request.user
        letter.save()
        messages.success(self.request, _('Your letter was updated successfully.'))
        return super(LetterUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your letter was not updated!'))
        return super(LetterUpdate, self).form_invalid(form)


class LetterDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Letter
    """
    model = Letter
    context_object_name = 'letter'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('resume:index')


class CareerList(LoginRequiredMixin, ListView):
    """
    Retrieve Career List
    """
    model = Career
    context_object_name = 'career_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        career_list = Career.objects.all()
        return career_list

    def get_context_data(self, **kwargs):
        context = super(CareerList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class CareerCreate(LoginRequiredMixin, CreateView):
    """
    Create Career
    """
    model = Career
    form_class = CareerForm
    http_method_names = ['get', 'post', ]
    success_url = reverse_lazy('resume:index')

    def form_valid(self, form):
        career = form.save(commit=False)
        career.writer = self.request.user
        career.save()
        messages.success(self.request, _('Your career was created successfully.'))
        return super(CareerCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(CareerCreate, self).form_invalid(form)


class CareerDetail(LoginRequiredMixin, DetailView):
    """
    Detail Career
    """
    model = Career
    context_object_name = 'career'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(CareerDetail, self).get_context_data(**kwargs)
        return context


class CareerUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Career
    """
    model = Career
    form_class = CareerForm
    context_object_name = 'career'
    http_method_names = ['get', 'post', ]

    def form_valid(self, form):
        career = form.save(commit=False)
        career.writer = self.request.user
        career.save()
        messages.success(self.request, _('Your career was updated successfully.'))
        return super(CareerUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your career was not updated!'))
        return super(CareerUpdate, self).form_invalid(form)


class CareerDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Career
    """
    model = Career
    context_object_name = 'career'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('resume:index')


class EducationList(LoginRequiredMixin, ListView):
    """
    Retrieve Education List
    """
    model = Education
    context_object_name = 'education_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        education_list = Education.objects.all()
        return education_list

    def get_context_data(self, **kwargs):
        context = super(EducationList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class EducationCreate(LoginRequiredMixin, CreateView):
    """
    Create Education
    """
    model = Education
    form_class = EducationForm
    http_method_names = ['get', 'post', ]
    success_url = reverse_lazy('resume:index')

    def form_valid(self, form):
        education = form.save(commit=False)
        education.writer = self.request.user
        education.save()
        messages.success(self.request, _('Your education was created successfully.'))
        return super(EducationCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(EducationCreate, self).form_invalid(form)


class EducationDetail(LoginRequiredMixin, DetailView):
    """
    Detail Education
    """
    model = Education
    context_object_name = 'education'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(EducationDetail, self).get_context_data(**kwargs)
        return context


class EducationUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Education
    """
    model = Education
    form_class = EducationForm
    context_object_name = 'education'
    http_method_names = ['get', 'post', ]

    def form_valid(self, form):
        education = form.save(commit=False)
        education.writer = self.request.user
        education.save()
        messages.success(self.request, _('Your education was updated successfully.'))
        return super(EducationUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your education was not updated!'))
        return super(EducationUpdate, self).form_invalid(form)


class EducationDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Education
    """
    model = Education
    context_object_name = 'education'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('resume:index')


class AwardList(LoginRequiredMixin, ListView):
    """
    Retrieve Award List
    """
    model = Award
    context_object_name = 'award_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        award_list = Award.objects.all()
        return award_list

    def get_context_data(self, **kwargs):
        context = super(AwardList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class AwardCreate(LoginRequiredMixin, CreateView):
    """
    Create Award
    """
    model = Award
    form_class = AwardForm
    http_method_names = ['get', 'post', ]
    success_url = reverse_lazy('resume:index')

    def form_valid(self, form):
        award = form.save(commit=False)
        award.writer = self.request.user
        award.save()
        messages.success(self.request, _('Your award was created successfully.'))
        return super(AwardCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(AwardCreate, self).form_invalid(form)


class AwardDetail(LoginRequiredMixin, DetailView):
    """
    Detail Award
    """
    model = Award
    context_object_name = 'award'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(AwardDetail, self).get_context_data(**kwargs)
        return context


class AwardUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Award
    """
    model = Award
    form_class = AwardForm
    context_object_name = 'award'
    http_method_names = ['get', 'post', ]

    def form_valid(self, form):
        award = form.save(commit=False)
        award.writer = self.request.user
        award.save()
        messages.success(self.request, _('Your award was updated successfully.'))
        return super(AwardUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your award was not updated!'))
        return super(AwardUpdate, self).form_invalid(form)


class AwardDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Award
    """
    model = Award
    context_object_name = 'award'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('resume:index')


class CertificateList(LoginRequiredMixin, ListView):
    """
    Retrieve Certificate List
    """
    model = Certificate
    context_object_name = 'certificate_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        certificate_list = Certificate.objects.all()
        return certificate_list

    def get_context_data(self, **kwargs):
        context = super(CertificateList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class CertificateCreate(LoginRequiredMixin, CreateView):
    """
    Create Certificate
    """
    model = Certificate
    form_class = CertificateForm
    http_method_names = ['get', 'post', ]
    success_url = reverse_lazy('resume:index')

    def form_valid(self, form):
        certificate = form.save(commit=False)
        certificate.writer = self.request.user
        certificate.save()
        messages.success(self.request, _('Your certificate was created successfully.'))
        return super(CertificateCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(CertificateCreate, self).form_invalid(form)


class CertificateDetail(LoginRequiredMixin, DetailView):
    """
    Detail Certificate
    """
    model = Certificate
    context_object_name = 'certificate'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(CertificateDetail, self).get_context_data(**kwargs)
        return context


class CertificateUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Certificate
    """
    model = Certificate
    form_class = CertificateForm
    context_object_name = 'certificate'
    http_method_names = ['get', 'post', ]

    def form_valid(self, form):
        certificate = form.save(commit=False)
        certificate.writer = self.request.user
        certificate.save()
        messages.success(self.request, _('Your certificate was updated successfully.'))
        return super(CertificateUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your certificate was not updated!'))
        return super(CertificateUpdate, self).form_invalid(form)


class CertificateDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Certificate
    """
    model = Certificate
    context_object_name = 'certificate'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('resume:index')


class LanguageList(LoginRequiredMixin, ListView):
    """
    Retrieve Language List
    """
    model = Language
    context_object_name = 'language_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        language_list = Language.objects.all()
        return language_list

    def get_context_data(self, **kwargs):
        context = super(LanguageList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class LanguageCreate(LoginRequiredMixin, CreateView):
    """
    Create Language
    """
    model = Language
    form_class = LanguageForm
    http_method_names = ['get', 'post', ]
    success_url = reverse_lazy('resume:index')

    def form_valid(self, form):
        language = form.save(commit=False)
        language.writer = self.request.user
        language.save()
        messages.success(self.request, _('Your language was created successfully.'))
        return super(LanguageCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(LanguageCreate, self).form_invalid(form)


class LanguageDetail(LoginRequiredMixin, DetailView):
    """
    Detail Language
    """
    model = Language
    context_object_name = 'language'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(LanguageDetail, self).get_context_data(**kwargs)
        return context


class LanguageUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Language
    """
    model = Language
    form_class = LanguageForm
    context_object_name = 'language'
    http_method_names = ['get', 'post', ]

    def form_valid(self, form):
        language = form.save(commit=False)
        language.writer = self.request.user
        language.save()
        messages.success(self.request, _('Your language was updated successfully.'))
        return super(LanguageUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your language was not updated!'))
        return super(LanguageUpdate, self).form_invalid(form)


class LanguageDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Language
    """
    model = Language
    context_object_name = 'language'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('resume:index')


class SkillList(LoginRequiredMixin, ListView):
    """
    Retrieve Skill List
    """
    model = Skill
    context_object_name = 'skill_list'
    http_method_names = ['get']
    paginate_by = 9

    def get_queryset(self):
        skill_list = Skill.objects.all()
        return skill_list

    def get_context_data(self, **kwargs):
        context = super(SkillList, self).get_context_data(**kwargs)
        context['title'] = _(resolve(self.request.path).app_name.capitalize())
        return context


class SkillCreate(LoginRequiredMixin, CreateView):
    """
    Create Skill
    """
    model = Skill
    form_class = SkillForm
    http_method_names = ['get', 'post', ]
    success_url = reverse_lazy('resume:index')

    def form_valid(self, form):
        skill = form.save(commit=False)
        skill.writer = self.request.user
        skill.save()
        messages.success(self.request, _('Your skill was created successfully.'))
        return super(SkillCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(SkillCreate, self).form_invalid(form)


class SkillDetail(LoginRequiredMixin, DetailView):
    """
    Detail Skill
    """
    model = Skill
    context_object_name = 'skill'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(SkillDetail, self).get_context_data(**kwargs)
        return context


class SkillUpdate(WriterOnlyMixin, UpdateView):
    """
    Update Skill
    """
    model = Skill
    form_class = SkillForm
    context_object_name = 'skill'
    http_method_names = ['get', 'post', ]

    def form_valid(self, form):
        skill = form.save(commit=False)
        skill.writer = self.request.user
        skill.save()
        messages.success(self.request, _('Your skill was updated successfully.'))
        return super(SkillUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Your skill was not updated!'))
        return super(SkillUpdate, self).form_invalid(form)


class SkillDelete(WriterOnlyMixin, DeleteView):
    """
    Delete Skill
    """
    model = Skill
    context_object_name = 'skill'
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('resume:index')

