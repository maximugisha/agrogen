from django import template
from django.utils.timesince import timesince

register = template.Library()


@register.filter
def in_list(value, the_list):
    return value in the_list

@register.filter
def short_timesince(value):
    time_str = timesince(value)
    time_parts = time_str.split(",")[0].split()

    if len(time_parts) == 2:
        number = time_parts[0]
        unit = time_parts[1]

        # Shorten units
        if 'minute' in unit:
            unit = 'm'
        elif 'hour' in unit:
            unit = 'h'
        elif 'day' in unit:
            unit = 'd'
        elif 'week' in unit:
            unit = 'w'
        elif 'month' in unit:
            unit = 'mo'
        elif 'year' in unit:
            unit = 'y'
        else:
            unit = 's'  # Default to seconds

        return f"{number}{unit}"

    return time_str