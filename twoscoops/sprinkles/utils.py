__author__ = 'plevytskyi'
from django.core.exceptions import PermissionDenied


def check_sprinkles(request):
    if (hasattr(request.user, 'can_sprinkle') and request.user.can_sprinkle) or request.user.is_staff:
        # By adding this value here it means our display templates
        # can be more generic. We don't need to have
        # {% if request.user.can_sprinkle or request.user.is_staff %}
        # instead just using
        # {% if request.can_sprinkle %}

        request.can_sprinkle = True
        return request

    # Return a HTTP 403 back to the user
    raise PermissionDenied