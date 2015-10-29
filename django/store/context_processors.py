from esite import settings
# from django.conf import settings
from models import Store

import logging
logger = logging.getLogger(__name__)

def ecomstore(request):
    """ context processor for the site templates """
    
    from django.utils import translation
    user_language = 'zh-cn'
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language

    try:
        store = Store.objects.get(code=settings.STORE_CODE)
    except Store.DoesNotExist:
        logger.debug('ecomstore - context processor failed to find store:' + settings.STORE_CODE)
        store = {}
        
    return {
            'active_store': store,
#             'analytics_tracking_id': settings.ANALYTICS_TRACKING_ID,
            'request': request
            }
