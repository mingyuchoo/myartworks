from django.contrib.auth.models import User
from django import forms
from taggit.forms import TagField, TagWidget
from core.widgets import BootstrapSelectInput, BootstrapTextInput, BootstrapTextarea
from .models import Profile, Friend


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  ]


class ProfileSimpleForm(forms.ModelForm):
    type = forms.ChoiceField(widget=forms.RadioSelect, choices=Profile.TYPE)
    nick_name = forms.CharField(widget=BootstrapTextInput(placeholder='Nick name'))
    class Meta:
        model = Profile
        fields = ['type',
                  'nick_name',
                  ]


class ProfileForm(forms.ModelForm):
    picture = forms.ClearableFileInput()
    type = forms.ChoiceField(widget=forms.RadioSelect, choices=Profile.TYPE)
    nick_name = forms.CharField(widget=BootstrapTextInput(placeholder='Nick name'))
    gender = forms.ChoiceField(widget=BootstrapSelectInput(), choices=Profile.GENDER)
    birth_date = forms.DateField(widget=BootstrapTextInput(placeholder='Birthday'))
    phone_number = forms.CharField(widget=BootstrapTextInput(attrs={'placeholder': '***-****-****'}), required=False)
    bio = forms.CharField(widget=BootstrapTextarea(placeholder='Biography'), required=False)
    status = forms.ChoiceField(widget=BootstrapSelectInput(), choices=Profile.STATUS)
    tags = TagField(widget=TagWidget(attrs={'class': 'form-control', 'placeholder': 'Tags'}))

    class Meta:
        model = Profile
        fields = ['picture',
                  'type',
                  'nick_name',
                  'gender',
                  'birth_date',
                  'phone_number',
                  'bio',
                  'tags'
                  ]


class FriendForm(forms.ModelForm):
    friend = forms.ModelChoiceField(widget=BootstrapSelectInput(), queryset=User.objects.all(), empty_label="(Nothing)")

    class Meta:
        model = Friend
        fields = ['friend']
