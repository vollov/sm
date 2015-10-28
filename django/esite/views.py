import logging
logger = logging.getLogger(__name__)

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render, redirect

from store.models import Store

def index(request):
    logger.debug('index.html - calling esite.views.index()')
    store = get_object_or_404(Store, code='10001')
    
    requestContext = RequestContext(request, {
        'page_title': 'Home',
        'store': store
    })
        
    return render(request, 'index.html', requestContext)
#     return redirect('products')
