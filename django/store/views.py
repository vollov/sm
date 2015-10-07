import logging
from django.shortcuts import render_to_response
from django.http import HttpResponse

logger = logging.getLogger(__name__)

from django.contrib.auth.decorators import login_required
from service import MenuService

from forms import StoreForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

@login_required
def profile(request):
    logger.debug('calling store.views.profile()')
    
    user_name = 'visitor'
    if request.user.is_authenticated():
        user_name = request.user.username
        logger.debug('page.views.profile() - user {0} login'.format(user_name))
    else:
        logger.debug('page.views.profile() - user not login')
        
    menu = MenuService.new_user_menu(request.user)
    context = {
        'menu':menu,
        'page_title': 'Profile',
        'user_name': user_name,
    }
    return render_to_response('profile.html', context)


@login_required
def create_store(request):
    logger.debug('calling store.views.create_store()')
    if request.method == 'POST':
        store_form = StoreForm(data=request.POST)
        if store_form.is_valid():
            store = store_form.save(commit=False)
#             store.owner = request.user.userProfile
            print 'user = {0}'.format(vars(request.user))
#             store.save()
            return store.views.owner_profile(request)
        else:
            print store_form.errors
            return HttpResponse("Create store is failed.")
    else:
        # for visitor, generate empty menu
        
        menu = MenuService.new_user_menu(request.user)
        
        store_form = StoreForm()
        
    requestContext = RequestContext(request, {'menu':menu,
                                              'store_form': store_form, 
                                              'page_title': 'Create Store'} )

    # Render the template depending on the context.
    return render_to_response('new.html', requestContext)

@login_required
def owner_profile(request):
    logger.debug('calling store.views.create_store()')

@login_required
def sales_profile(request):
    logger.debug('calling store.views.create_store()')
        
@login_required
def mix_profile(request):
    logger.debug('calling store.views.create_store()')



@login_required
#@permission_required('store.enlist')
def store_list(request, user_id):
    """
    Verify user has the access to enlist store.
    """
    logger.debug('calling store.views.store_list()')
    user_name = request.user.username
    
    menu = MenuService.new_user_menu(request.user)
    context = {
        'menu':menu,
        'page_title': 'Profile',
        'user_name': user_name,
    }
    return render_to_response('profile.html', context)


@login_required
#@permission_required('store.edit')
def store_edit(request, user_id, store_id):
    logger.debug('calling store.views.store_list()')


class ProfileHelper:
    """
    Helper class to check user status and direct the view names
    """
    
    def isStoreOwner(self, user):
        """ check if the user own stores, return true if user own store"""
        
    def isSales(self, user):
        """ check if the user is a sales under a stores, return true if user is sales"""
        
    def getOwnedStores(self, user):
        """ fetch list of stores a user owned"""
        
    def getJoinedStores(self,user):
        """ fetch list of stores a user joined"""