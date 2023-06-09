from django import template

register = template.Library()


@register.inclusion_tag("Products/temtag/ratings-templatetags.html")
def ratings_show(objects):
    return {
        "object": objects.rate
    }


@register.inclusion_tag("Products/temtag/ratings-templatetags-ltr.html")
def average_rate(objects):
    try:
        num = 0
        sums = 0
        for i in objects:
            num += 1
            sums += i.rate
        objects = round(sums / num)
        return {
            "object": objects
        }
    except ZeroDivisionError:
        return {
            "object": 1
        }