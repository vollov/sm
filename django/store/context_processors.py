from esite import settings
# from django.conf import settings
from models import Store
from django.contrib.auth.models import Group

import logging
logger = logging.getLogger(__name__)

def ecomstore(request):
    """ context processor for the site templates """
    
    from django.utils import translation
    user_language = 'zh-cn'
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    
    manu_items = {}
    manu_items['menu.products'] = '/store/products/'
    
    if request.user.is_authenticated():
        main_menu(request.user, manu_items)
        
    try:
        store = Store.objects.get(code=settings.STORE_CODE)
    except Store.DoesNotExist:
        logger.debug('ecomstore - context processor failed to find store:' + settings.STORE_CODE)
        store = {}
    
    return {
            'active_store': store,
            'user':request.user,
            'manu_items': manu_items,
#             'analytics_tracking_id': settings.ANALYTICS_TRACKING_ID,
            'request': request
            }

def main_menu(user, manu_items):
    """
    return a dictionary {'name', 'url'} for show menu
    """
    
    group = Group.objects.get(name='owner')
    if group in user.groups.all():
        manu_items['menu.orders'] = '/store/orders/'
            
    
#     return manu_items