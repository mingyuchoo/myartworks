from django import forms
from django.contrib.auth.models import User
from taggit.forms import TagField, TagWidget
from core.widgets import BootstrapSelectInput, BootstrapSelectMultiple, BootstrapTextInput, BootstrapTextarea
from .models import Team, Membership, Comment


class TeamCreateForm(forms.ModelForm):
    """
    Team form
    """
    name = forms.CharField(widget=BootstrapTextInput(placeholder='Name'))
    description = forms.CharField(widget=BootstrapTextarea(placeholder='Description'))
    tags = TagField(widget=TagWidget(attrs={'class': 'form-control', 'placeholder': 'Tags'}))

    class Meta:
        model = Team
        fields = ['name', 'description', 'tags']


class TeamUpdateForm(forms.ModelForm):
    """
    Team form
    """
    name = forms.CharField(widget=BootstrapTextInput(placeholder='Name'))
    description = forms.CharField(widget=BootstrapTextarea(placeholder='Description'))
    leader = forms.ModelChoiceField(widget=BootstrapSelectInput(), queryset=User.objects.all())
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=Team.STATUS)
    tags = TagField(widget=TagWidget(attrs={'class': 'form-control', 'placeholder': 'Tags'}))

    class Meta:
        model = Team
        fields = ['name', 'description', 'leader', 'status', 'tags']


class MembershipUpdateForm(forms.ModelForm):
    """
    Membership update form
    """
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=Membership.STATUS)

    class Meta:
        model = Membership
        fields = ['status', ]


class CommentForm(forms.ModelForm):
    """
    Comment form
    """
    content = forms.CharField(widget=BootstrapTextInput(placeholder='Content'))

    class Meta:
        model = Comment
        fields = ['content', ]
