import logging
from django.shortcuts import render_to_response

logger = logging.getLogger(__name__)

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    logger.debug('calling page.views.profile()')
    
    user_name = 'visitor'
    if not request.user.is_authenticated():
        user_name = request.user.username
        
    context = {
        'page_title': 'Profile',
        'user_name': user_name,
    }
    return render_to_response('profile.html', context)
