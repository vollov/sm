import logging
logger = logging.getLogger(__name__)

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from django.shortcuts import render, redirect

def index(request):
    logger.debug('index.html - calling esite.views.index()')

    return redirect('store.views.products')
