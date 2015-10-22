import logging
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

logger = logging.getLogger(__name__)

from django.contrib.auth.decorators import login_required
from service import MenuService

from forms import StoreForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from .models import Store, StoreEnrollment
from sales.models import Customer


@login_required
def create_store(request):
    logger.debug('calling store.views.create_store()')
    if request.method == 'POST':
        store_form = StoreForm(data=request.POST)
        if store_form.is_valid():
            store = store_form.save(commit=False)
            store.owner = request.user
            print 'user = {0}'.format(vars(request.user))
            store.save()
            return owner_profile(request)
        else:
            print store_form.errors
            return HttpResponse("Create store is failed.")
    else:
        # for visitor, generate empty menu
        
        menu = MenuService.new_user_menu(request.user)
        
        store_form = StoreForm()
        
    requestContext = RequestContext(request, {'menu':menu,
                                              'store_form': store_form, 
                                              'page_title': 'Create store'} )

    # Render the template depending on the context.
    return render_to_response('new.html', requestContext)

class Enrollment:
    
    def __init__(self, id, username, email, status):
        self.id = id
        self.username = username
        self.email = email
        self.status = status
        
@login_required
def profile(request):
    logger.debug('calling store.views.profile()')
    
    user_name = 'visitor'
#     if request.user.is_authenticated():
#         current_user = request.user
#         logger.debug('page.views.profile() - user {0} login'.format(current_user.username))
#     else:
#         logger.debug('page.views.profile() - user not login')
    
#     print 'user = {0}'.format(vars(request.user))   
    menu = MenuService.new_user_menu(request.user)
    context = {
        'menu':menu,
        'page_title': 'User profile',
        'user': request.user,
    }
    return render_to_response('profile.html', context)


@login_required
def owner_profile(request):
    """
    Default view show list of sales person in store, button to enable/disable sales.
    TODO: show store statistics: 
    1.number of customers
    2.number of orders
    3.total profits
    4.return ratio
    """
    
    store = request.session['current_store']
    
    #list sales agents
    enrollments = StoreEnrollment.objects.filter(store_id = store.id)
    
    enrolls = []
    for item in enrollments:
        enroll = Enrollment(item.id, item.agent.username, item.agent.email, item.active)
#         user = User.objects.get(id = enroll.agent.id)
        enrolls.append(enroll)
    
    # compute the menu
    menu = MenuService.owner_menu(request.user, store)
    
    logger.debug('calling store.views.owner_profile()')
    requestContext = RequestContext(request, {'menu':menu,
                                              'store':store,
                                              'enrolls': enrolls,
                                              'user': request.user, 
                                              'page_title': 'Owner profile'} )

    return render_to_response('owner-profile.html', requestContext)

@login_required
def unapproved_agent_profile(request):
    menu = MenuService.unapproved_sales_menu(request.user, store)
    store = request.session['current_store']
    logger.debug('calling store.views.unapproved_agent_profile()')
        
    requestContext = RequestContext(request, {'menu':menu,
                                              'store':store,
                                              'user': request.user, 
                                              'page_title': 'Unapproved agent profile'} )

    return render_to_response('unapproved-agent-profile.html', requestContext)

@login_required
def agent_profile(request):
    """
    Default view show list of customers, order button for customer.
    TODO: show store statistics: 
    1.number of customers
    2.number of orders
    3.total profits
    4.return ratio
    """
    
    # list all customer of this agent
    user = request.user
    customers = Customer.objects.filter(agent_id = user.id,store_id = store.id)
    store = request.session['current_store']
    
    # compute the menu
    menu = MenuService.sales_menu(request.user, store)    
    
    logger.debug('calling store.views.agent_profile()')
        
    requestContext = RequestContext(request, {'menu':menu,
                                              'customers': customers,
                                              'store':store,
                                              'user': request.user, 
                                              'page_title': 'Agent profile'} )

    return render_to_response('agent-profile.html', requestContext)

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



class ProfileViewHelper:
    """
    Helper class to check user status and direct the view names
    """
    def __init__(self, user):
        self._user = user
    
    
    def direct_view(self, request):
        """direct view
        
        return a dict for profile to process {'view_url': m, 'template':t ,'store_id': s }
        
        directly call view method
        
        sessions:
        fav_color = request.session['fav_color']
        request.session['has_commented'] = True
        del request.session['member_id']
        
        """

        request.session['current_user'] = self._user
         
        owned_store = self.get_owned_stores()
        joined_store = self.get_joined_stores()
        if owned_store:
            # view owner_profile
            request.session['current_store'] = owned_store
            
#             HttpResponseRedirect('/store/owner/')
            return owner_profile(request)
        
        if joined_store:
            # view sales_profile
            #
            request.session['current_store'] = joined_store
            
            if self.is_approved_agent(joined_store.id):
#                 HttpResponseRedirect('/store/agent/')
                return agent_profile(request)
            else:
#                 HttpResponseRedirect('/store/unapproved-agent/')
                return unapproved_agent_profile(request)
        
        # view profile()    
        HttpResponseRedirect('/store/profile/')
#         return profile(request)
        
        
    def is_owner(self):
        """ check if the user own stores, return true if user own store"""
        return True
        
    def is_approved_agent(self, store_id):
        """ check if the agent is approved by owner"""
        enrollments = StoreEnrollment.objects.filter(store_id = store_id, agent_id=self._user.id, active=True)
        if enrollments:
            return True
        else:
            return False
        
    def get_owned_stores(self):
        """ fetch list of stores a user owned"""
        user_id = self._user.id
        stores = Store.objects.filter(owner__id=user_id)
        if stores:
            return stores[0]
        else:
            return None

    def get_joined_stores(self):
        """ fetch list of stores a user joined"""
        user_id = self._user.id
        stores = Store.objects.filter(sales__id=user_id)
        if stores:
            return stores[0]
        else:
            return None
        
@login_required
def add_customer(request, store_id):
    """
    agent can add user after login.
    
    method assumes user is already approved. 
    """
    user = request.user
    
    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST)
        if profile_form.is_valid():
            user_profile = profile_form.save(commit=False)
            user_profile.user=user
            user_profile.save()
            return store.views.profile(request) 
        else:
            print profile_form.errors
#             return HttpResponse("Edit profile is failed.")
            raise Http404("Edit profile is failed.")
    else:
        # for visitor, generate empty menu
        menu = MenuService.visitor_menu()
        profile_form = UserProfileForm()
    requestContext = RequestContext(request, {'menu':menu,
                                              'page_title': 'Edit Profile',
                                              'profile_form': profile_form} )