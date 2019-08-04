from django import template
register = template.Library()

@register.filter
def error(errors): #retorna el primer error del campo
    if errors:
        for i in errors:
            return i
    else:
        return ''       

@register.filter
def invalid(error, class_='is-invalid'): #verificacion del error
    return '' if not error else class_

@register.filter
def select(value='', real='-'): #selecciona el valor correspondiente
    return 'selected' if value == real else ''

@register.filter
def booleanSelect(value, real):
    return 'selected' if value is real else ''

@register.filter
def radio(value='', real='-'): #checkea el valor correspondiente
    return 'checked' if value == real else ''

@register.filter
def old(value): #checkea el valor correspondiente
    return value if value else ''

@register.filter
def substring(value, size): #retorna un string recortado con longitud igual a size
    return value[:size]+' ...' if len(value) > size else value+'.'

@register.filter
def is_in(var, args):
    if args is None:
        return False
    arg_list = [arg.strip() for arg in args.split(',')]
    return var in arg_list



