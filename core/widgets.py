from django import forms


class BootstrapSelectInput(forms.Select):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs.setdefault('class', 'form-control')

        super(BootstrapSelectInput, self).__init__(attrs=attrs)


class BootstrapSelectMultiple(forms.SelectMultiple):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs.setdefault('class', 'form-control')

        super(BootstrapSelectMultiple, self).__init__(attrs=attrs)


class BootstrapTextInput(forms.TextInput):
    def __init__(self, attrs=None, placeholder=None):
        if attrs is None:
            attrs = {}
        attrs.setdefault('class', 'form-control')
        if placeholder:
            attrs['placeholder'] = placeholder

        super(BootstrapTextInput, self).__init__(attrs=attrs)


class BootstrapTextarea(forms.Textarea):
    def __init__(self, attrs=None, placeholder=None):
        if attrs is None:
            attrs = {}
        attrs.setdefault('class', 'form-control')
        if placeholder:
            attrs['placeholder'] = placeholder

        super(BootstrapTextarea, self).__init__(attrs=attrs)


class BootstrapPasswordInput(forms.PasswordInput):
    def __init__(self, attrs=None, placeholder=None):
        if attrs is None:
            attrs = {}
        attrs.setdefault('class', 'form-control')
        if placeholder:
            attrs['placeholder'] = placeholder

        super(BootstrapPasswordInput, self).__init__(attrs=attrs)


class BootstrapNumberInput(forms.NumberInput):
    def __init__(self, attrs=None, placeholder=None):
        if attrs is None:
            attrs = {}
        attrs.setdefault('class', 'form-control')
        if placeholder:
            attrs['placeholder'] = placeholder

        super(BootstrapNumberInput, self).__init__(attrs=attrs)


class BootstrapEmailInput(forms.EmailInput):
    def __init__(self, attrs=None, placeholder=None):
        if attrs is None:
            attrs = {}
        attrs.setdefault('class', 'form-control')
        if placeholder:
            attrs['placeholder'] = placeholder

        super(BootstrapEmailInput, self).__init__(attrs=attrs)

