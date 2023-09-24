from django import template
from django.contrib.auth import get_user_model
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
user_model = get_user_model()

register = template.Library()
@register.filter
def author_details(author):
    if not isinstance(author, user_model):
        return ""
    if author.first_name and author.last_name:
        name=f"{author.first_name} {author.last_name}"
    else:
        name=f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""
    return mark_safe(f"{prefix}{name}{suffix}")
