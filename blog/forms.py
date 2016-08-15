from django import forms

from core.widgets import BootstrapTextInput, BootstrapTextarea
from .models import Section, Post, Comment


class PostForm(forms.ModelForm):
    """
    Post form
    """
    image = forms.ImageField(required=True)
    title = forms.CharField(widget=BootstrapTextInput(placeholder='Title'))
    content = forms.CharField(widget=BootstrapTextarea(placeholder='Content'))

    class Meta:
        model = Post
        fields = ['title', 'image', 'content', ]


class CommentForm(forms.ModelForm):
    """
    Comment form
    """
    content = forms.CharField(widget=BootstrapTextInput(placeholder='Content'))

    class Meta:
        model = Comment
        fields = ['content', ]
