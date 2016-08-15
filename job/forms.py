from django import forms
from taggit.forms import TagField, TagWidget
from core.widgets import BootstrapTextInput, BootstrapTextarea
from .models import Work, Comment


class WorkCreateForm(forms.ModelForm):
    """
    Work Create form
    """
    image = forms.ImageField(required=True)
    title = forms.CharField(widget=BootstrapTextInput(placeholder='Title'))
    description = forms.CharField(widget=BootstrapTextarea(placeholder='Description'))
    tags = TagField(widget=TagWidget(attrs={'class': 'form-control', 'placeholder': 'Tags'}))

    class Meta:
        model = Work
        fields = ['image', 'title', 'description', 'tags']


class WorkUpdateForm(forms.ModelForm):
    """
    Work Update form
    """
    description = forms.CharField(widget=BootstrapTextarea(placeholder='Description'))
    tags = TagField(widget=TagWidget(attrs={'class': 'form-control', 'placeholder': 'Tags'}))

    class Meta:
        model = Work
        fields = ['description', 'tags']


class CommentForm(forms.ModelForm):
    """
    Comment form
    """
    content = forms.CharField(widget=BootstrapTextInput(placeholder='Content'))

    class Meta:
        model = Comment
        fields = ['content', ]
