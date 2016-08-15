import copy
from itertools import chain

from django.forms.utils import flatatt
from django.forms.widgets import Widget
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class Dropdown(Widget):
    """
    Dropdown Widget
    """
    allow_multiple_selected = False

    def __init__(self, attrs=None, choices=()):
        super(Dropdown, self).__init__(attrs)
        # choices can be any iterable, but we may need to render this widget
        # multiple times. Thus, collapse it into a list so it can be consumed
        # more than once.
        self.choices = list(choices)
        self.title = None

    def __deepcopy__(self, memo):
        obj = copy.copy(self)
        obj.attrs = self.attrs.copy()
        obj.choices = copy.copy(self.choices)
        memo[id(self)] = obj
        return obj

    def render(self, name, value, attrs=None, choices=()):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        if self.title is None:
            self.title = ''.join(['-- ', final_attrs['name'], ' --'])
        options = self.render_options(choices, [value])

        output = [format_html(
            '<div class="btn-group">'
            '<a href="#" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">'
            '{}&nbsp;&nbsp;&nbsp;<span class="caret"></span></a><ul class="dropdown-menu" {}>',
            self.title.capitalize(),
            flatatt(final_attrs))]
        if options:
            output.append(options)
        output.append('</ul></div>')
        return mark_safe('\n'.join(output))

    def render_option(self, selected_choices, option_value, option_label):
        if option_value is None:
            option_value = ''
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' class="active"')
            self.title = force_text(option_label)
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        return format_html('<li {}><a><option value="{}">{}</option></a></li>',
                           selected_html,
                           option_value,
                           force_text(option_label))

    def render_options(self, choices, selected_choices):
        # Normalize to strings.
        selected_choices = set(force_text(v) for v in selected_choices)
        output = []
        for option_value, option_label in chain(self.choices, choices):
            if isinstance(option_label, (list, tuple)):
                output.append(format_html('<optgroup label="{}">', force_text(option_value)))
                for option in option_label:
                    output.append(self.render_option(selected_choices, *option))
                output.append('</optgroup>')
            else:
                output.append(self.render_option(selected_choices, option_value, option_label))
        return '\n'.join(output)
