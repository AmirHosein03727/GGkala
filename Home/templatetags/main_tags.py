from django import template

register = template.Library()


@register.simple_tag
def fa_number(number):
    farsi_num = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹',
    }

    for a, b in farsi_num.items():
        number = str(number).replace(a, b)

    return number
