from django import template
register = template.Library()

@register.filter
def error(errors): 
    """ returns the first field error """
    if errors:
        for i in errors:
            return i
    else:
        return ''       

@register.filter
def invalid(error, class_='is-invalid'):
    """ verification of the error """
    return '' if not error else class_

@register.filter
def select(value='', real='-'):
    """ select the corresponding value """
    return 'selected' if value == real else ''

@register.filter
def booleanSelect(value, real):
    """ check the corresponding value """
    return 'selected' if value is real else ''

@register.filter
def radio(value='', real='-'):
    """ check the corresponding value """
    return 'checked' if value == real else ''

@register.filter
def old(value):
    """ check the corresponding value """
    return value if value else ''

@register.filter
def substring(value, size):
    """ returns a trimmed string with length equal to size """
    return value[:size]+' ...' if len(value) > size else value+'.'

@register.filter
def activity_count_comments(activity, value):
    """ returns the value of count_comments """
    return activity.count_comments(value)











