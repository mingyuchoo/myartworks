from django import forms

from core.widgets import BootstrapEmailInput, BootstrapTextInput, BootstrapTextarea


class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=BootstrapEmailInput(placeholder='From'))
    subject = forms.CharField(widget=BootstrapTextInput(placeholder='Subject'))
    message = forms.CharField(widget=BootstrapTextarea(placeholder='Message'), required=False)
