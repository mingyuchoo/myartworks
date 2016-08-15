from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from core.widgets import BootstrapTextInput, BootstrapTextarea

from .models import Message


class MessageSendForm(forms.ModelForm):
    """
    Message Send form
    """
    receiver = forms.CharField(widget=BootstrapTextInput(placeholder=_('Receiver')))
    content = forms.CharField(widget=BootstrapTextarea())

    class Meta:
        model = Message
        fields = ['receiver', 'content', ]

    def clean(self):
        receiver = self.cleaned_data.get('receiver')
        if not receiver:
            raise forms.ValidationError('Must specify receiver.')
        if receiver:
            receiver = User.objects.get(username=receiver)
            self.cleaned_data['receiver'] = receiver
        return super(MessageSendForm, self).clean()


class MessageReplyForm(forms.ModelForm):
    """
    Message Reply form
    """
    content = forms.CharField(widget=BootstrapTextarea())

    class Meta:
        model = Message
        fields = ['content', ]
