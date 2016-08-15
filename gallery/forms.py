from django import forms
from taggit.forms import TagField, TagWidget

from core.widgets import BootstrapTextInput, BootstrapTextarea
from .models import Portfolio, Comment


class PortfolioCreateForm(forms.ModelForm):
    """
    Portfolio Create form
    """
    image = forms.ImageField(required=True)
    resource = forms.FileField(widget=forms.FileInput, required=False)
    title = forms.CharField(widget=BootstrapTextInput(placeholder='Title'))
    content = forms.CharField(widget=BootstrapTextarea(placeholder='Content'))
    tags = TagField(widget=TagWidget(attrs={'class': 'form-control', 'placeholder': 'Tags'}))

    class Meta:
        model = Portfolio
        fields = ['image', 'resource', 'title', 'content', 'tags']


class PortfolioUpdateForm(forms.ModelForm):
    """
    Portfolio Update form
    """
    title = forms.CharField(widget=BootstrapTextInput(placeholder='Title'))
    content = forms.CharField(widget=BootstrapTextarea(placeholder='Content'))
    tags = TagField(widget=TagWidget(attrs={'class': 'form-control', 'placeholder': 'Tags'}))

    class Meta:
        model = Portfolio
        fields = ['title', 'content', 'tags']


class CommentForm(forms.ModelForm):
    """
    Comment form
    """
    content = forms.CharField(widget=BootstrapTextInput(placeholder='Content'))

    class Meta:
        model = Comment
        fields = ['content', ]
