from django.template import Library

from templates_advanced.profiles.models import Profile

register = Library()


@register.inclusion_tag('tags/profile_complete_notification.html', takes_context=True)
def profile_complete_notification(context):
    is_complete = True
    if context.request.user.id:
        profile = Profile.objects.get(pk=context.request.user.id)
    return {
        'is_complete': is_complete,
    }
