from __future__ import unicode_literals

import copy
from django.core.exceptions import ValidationError
# Provide this import for backwards compatibility.
from django.forms.fields import Field
from django.utils.encoding import force_text, smart_text
from django.utils.translation import ugettext_lazy as _

from core.forms.widgets import Dropdown


class CallableDropdownIterator(object):
    """
    Collable Dropdown Iterator
    """
    def __init__(self, choices_func):
        self.choices_func = choices_func

    def __iter__(self):
        for e in self.choices_func():
            yield e


class DropdownField(Field):
    """
    Dropdown Field Widget
    """
    widget = Dropdown
    default_error_messages = {
        'invalid_choice': _('Dropdown a valid choice. %(value)s is not one of the available choices.'),
    }

    def __init__(self, choices=(), required=True, widget=None, label=None,
                 initial=None, help_text='', *args, **kwargs):
        super(DropdownField, self).__init__(required=required, widget=widget, label=label,
                                            initial=initial, help_text=help_text, *args, **kwargs)
        self.choices = choices

    def __deepcopy__(self, memo):
        result = super(DropdownField, self).__deepcopy__(memo)
        result._choices = copy.deepcopy(self._choices, memo)
        return result

    def _get_choices(self):
        return self._choices

    def _set_choices(self, value):
        # Setting choices also sets the choices on the widget.
        # choices can be any iterable, but we call list() on it because
        # it will be consumed more than once.
        if callable(value):
            value = CallableDropdownIterator(value)
        else:
            value = list(value)

        self._choices = self.widget.choices = value

    choices = property(_get_choices, _set_choices)

    def to_python(self, value):
        """Returns a Unicode object."""
        if value in self.empty_values:
            return ''
        return smart_text(value)

    def validate(self, value):
        """Validates that the input is in self.choices."""
        super(DropdownField, self).validate(value)
        if value and not self.valid_value(value):
            raise ValidationError(
                self.error_messages['invalid_choice'],
                code='invalid_choice',
                params={'value': value},
            )

    def valid_value(self, value):
        """Check to see if the provided value is a valid choice"""
        text_value = force_text(value)
        for k, v in self.choices:
            if isinstance(v, (list, tuple)):
                # This is an optgroup, so look inside the group for options
                for k2, v2 in v:
                    if value == k2 or text_value == force_text(k2):
                        return True
            else:
                if value == k or text_value == force_text(k):
                    return True
        return False
