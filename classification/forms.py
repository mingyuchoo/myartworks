from django import forms

from core.widgets import BootstrapTextInput
from .models import Category, Field


class CategoryForm(forms.ModelForm):
    """
    Category Create form
    """
    name = forms.CharField(widget=BootstrapTextInput(placeholder='Name'))

    class Meta:
        model = Category
        fields = ['name', ]


class FieldForm(forms.ModelForm):
    """
    Field Create form
    """
    name = forms.CharField(widget=BootstrapTextInput(placeholder='Name'))

    class Meta:
        model = Field
        fields = ['name', ]
