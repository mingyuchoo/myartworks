from django import forms
from datetime import date

from core.widgets import BootstrapTextInput, BootstrapTextarea
from .models import (Basic,
                     Contact,
                     Letter,
                     Career,
                     Education,
                     Award,
                     Certificate,
                     Language,
                     Skill
                     )


class BasicForm(forms.ModelForm):
    """
    Basic form
    """
    full_name = forms.CharField(widget=BootstrapTextInput(placeholder='Full Name'), required=False)
    job_title = forms.CharField(widget=BootstrapTextInput(placeholder='Job Title'), required=False)
    location = forms.CharField(widget=BootstrapTextInput(placeholder='Location'), required=False)

    class Meta:
        model = Basic
        fields = ['full_name',
                  'job_title',
                  'location',
                  ]


class ContactForm(forms.ModelForm):
    """
    Contact form
    """
    email = forms.CharField(widget=BootstrapTextInput(placeholder='E-mail Address'), required=False)
    phone1 = forms.CharField(widget=BootstrapTextInput(placeholder='Phone 1'), required=False)
    phone2 = forms.CharField(widget=BootstrapTextInput(placeholder='Phone 2'), required=False)
    website = forms.CharField(widget=BootstrapTextInput(placeholder='Website'), required=False)

    class Meta:
        model = Contact
        fields = ['email',
                  'phone1',
                  'phone2',
                  'website',
                  ]


class LetterForm(forms.ModelForm):
    """
    Letter form
    """
    content = forms.CharField(widget=BootstrapTextarea(placeholder='Content'), required=False)

    class Meta:
        model = Letter
        fields = ['content',
                  ]


class CareerForm(forms.ModelForm):
    """
    Career form
    """
    company = forms.CharField(widget=BootstrapTextInput(placeholder='Company'))
    website = forms.CharField(widget=BootstrapTextInput(placeholder='Website'), required=False)
    location = forms.CharField(widget=BootstrapTextInput(placeholder='Location'), required=False)
    position = forms.CharField(widget=BootstrapTextInput(placeholder='Job Position'))
    start_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, date.today().year)))
    end_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, date.today().year)))
    details = forms.CharField(widget=BootstrapTextarea(placeholder='Details'))

    class Meta:
        model = Career
        fields = ['company',
                  'website',
                  'location',
                  'position',
                  'start_date',
                  'end_date',
                  'details',
                  ]


class EducationForm(forms.ModelForm):
    """
    Education form
    """
    school = forms.CharField(widget=BootstrapTextInput(placeholder='School'))
    website = forms.CharField(widget=BootstrapTextInput(placeholder='Website'), required=False)
    location = forms.CharField(widget=BootstrapTextInput(placeholder='Location'), required=False)
    degree = forms.CharField(widget=BootstrapTextInput(placeholder='Degree'))
    start_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, date.today().year)))
    end_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, date.today().year)))
    details = forms.CharField(widget=BootstrapTextarea(placeholder='Details'))

    class Meta:
        model = Education
        fields = ['school',
                  'website',
                  'location',
                  'degree',
                  'start_date',
                  'end_date',
                  'details',
                  ]


class AwardForm(forms.ModelForm):
    """
    Award form
    """
    title = forms.CharField(widget=BootstrapTextInput(placeholder='Title'))
    organization = forms.CharField(widget=BootstrapTextInput(placeholder='Organization'))
    website = forms.CharField(widget=BootstrapTextInput(placeholder='Website'), required=False)

    class Meta:
        model = Award
        fields = ['title',
                  'organization',
                  'website',
                  ]


class CertificateForm(forms.ModelForm):
    """
    Certificate form
    """
    title = forms.CharField(widget=BootstrapTextInput(placeholder='Title'))
    level = forms.CharField(widget=BootstrapTextInput(placeholder='Level'))
    organization = forms.CharField(widget=BootstrapTextInput(placeholder='Organization'))
    website = forms.CharField(widget=BootstrapTextInput(placeholder='Website'), required=False)
    acquisition_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, date.today().year)))

    class Meta:
        model = Certificate
        fields = ['title',
                  'level',
                  'organization',
                  'website',
                  'acquisition_date',
                  ]


class LanguageForm(forms.ModelForm):
    """
    Language form
    """
    name = forms.CharField(widget=BootstrapTextInput(placeholder='Name'))
    level = forms.CharField(widget=BootstrapTextInput(placeholder='Level'))

    class Meta:
        model = Language
        fields = ['name',
                  'level',
                  ]


class SkillForm(forms.ModelForm):
    """
    Skill form
    """
    name = forms.CharField(widget=BootstrapTextInput(placeholder='Name'))
    level = forms.CharField(widget=BootstrapTextInput(placeholder='Level'))

    class Meta:
        model = Skill
        fields = ['name',
                  'level',
                  ]
