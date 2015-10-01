import logging
from django.shortcuts import render_to_response

logger = logging.getLogger(__name__)

def profile(request):
    logger.debug('calling page.views.profile()')

    context = {
        'page_title': 'Profile',
    }
    return render_to_response('profile.html', context)
