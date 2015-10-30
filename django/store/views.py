import logging
logger = logging.getLogger(__name__)
from django.utils.translation import ugettext as _

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

from models import Product, Order, ProductOrder

def products(request):
    """
    Show products to public
    """
    logger.debug('products.html - calling store.views.products()')
    
    products = Product.objects.filter(active=True)
    
    for product in products:
        thumbnails = product.image_set.filter(is_thumbnail=True)
        if thumbnails:
            product.thumbnail = thumbnails[0]
        else:
            product.thumbnail = 'na.jpg'
                   
    requestContext = RequestContext(request, {
        'page_title': 'Products',
        'products': products,
    })
        
    return render_to_response('products.html', requestContext)

def product_detail(request, sku):
    """
    Show product detail by sku to public
    """
    logger.debug('product-detail.html - calling store.views.product_detail()')
    
    product = get_object_or_404(Product, sku=sku)
    thumbnails = product.image_set.filter(is_thumbnail=True)
    if thumbnails:
        product.thumbnail = thumbnails[0]
    else:
        product.thumbnail = 'na.jpg'
        
    images = product.image_set.filter(active=True)
    
    requestContext = RequestContext(request, {
        'page_title': 'Product detail',
        'product':product,
        'images': images,
    })
    
    return render_to_response('product-detail.html', requestContext)
    
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def logout_view(request):
    logger.debug('calling store.views.logout_view()')
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def orders(request):
    """
    list orders for owner
    """

    orders = Order.objects.all()
     
    requestContext = RequestContext(request, {
                                              'orders': orders,
                                              'page_title': _('menu.orders')} )
          
    return render_to_response('orders.html', requestContext)

@login_required
def order_detail(request, order_id):
     
    order = get_object_or_404(Order, pk=order_id)
    product_orders = ProductOrder.objects.filter(order_id=order_id)
    requestContext = RequestContext(request, {
                                          'product_orders': product_orders,
                                          'order':order,
                                          'page_title': 'order detail'} )

    return render_to_response('order-detail.html', requestContext)
# 

# import logging
# from django.shortcuts import render_to_response
# from django.http import HttpResponse, HttpResponseRedirect
# 
# logger = logging.getLogger(__name__)
# 
# from django.contrib.auth.decorators import login_required
# from service import MenuService
# 
# from forms import StoreForm
# from django.shortcuts import render_to_response, get_object_or_404
# from django.template import RequestContext
# 
# from .models import Store, StoreEnrollment
# from sales.models import Customer

# @login_required
# def create_store(request):
#     logger.debug('calling store.views.create_store()')
#     if request.method == 'POST':
#         store_form = StoreForm(data=request.POST)
#         if store_form.is_valid():
#             store = store_form.save(commit=False)
#             store.owner = request.user
#             print 'user = {0}'.format(vars(request.user))
#             store.save()
#             return owner_profile(request)
#         else:
#             print store_form.errors
#             return HttpResponse("Create store is failed.")
#     else:
#         # for visitor, generate empty menu
#         
#         menu = MenuService.new_user_menu(request.user)
#         
#         store_form = StoreForm()
#         
#     requestContext = RequestContext(request, {'menu':menu,
#                                               'store_form': store_form, 
#                                               'page_title': 'Create store'} )
# 
#     # Render the template depending on the context.
#     return render_to_response('new.html', requestContext)
# 
# class Enrollment:
#     
#     def __init__(self, id, username, email, status):
#         self.id = id
#         self.username = username
#         self.email = email
#         self.status = status
#         
# @login_required
# def profile(request):
#     logger.debug('calling store.views.profile()')
#     
#     menu = MenuService.new_user_menu(request.user)
#     context = {
#         'menu':menu,
#         'page_title': 'User profile',
#         'user': request.user,
#     }
#     return render_to_response('profile.html', context)
# 
# 
# @login_required
# def owner_profile(request):
#     """
#     Default view show list of sales person in store, button to enable/disable sales.
#     TODO: show store statistics: 
#     1.number of customers
#     2.number of orders
#     3.total profits
#     4.return ratio
#     """
#     
#     store_id = request.session['current_store_id']
#     store = Store.objects.get(id = store_id)
#     #list sales agents
#     enrollments = StoreEnrollment.objects.filter(store_id = store_id)
#     
#     enrolls = []
#     for item in enrollments:
#         enroll = Enrollment(item.id, item.agent.username, item.agent.email, item.active)
# #         user = User.objects.get(id = enroll.agent.id)
#         enrolls.append(enroll)
#     
#     # compute the menu
#     menu = MenuService.owner_menu(request.user, store)
#     
#     request.session['current_menu'] = menu
#     
#     logger.debug('calling store.views.owner_profile()')
#     requestContext = RequestContext(request, {'menu':menu,
#                                               'store':store,
#                                               'enrolls': enrolls,
#                                               'user': request.user, 
#                                               'page_title': 'Owner profile'} )
# 
#     return render_to_response('owner-profile.html', requestContext)
# 
# @login_required
# def unapproved_agent_profile(request):
#     store_id = request.session['current_store_id']
#     store = Store.objects.get(id = store_id)
#     
#     menu = MenuService.unapproved_sales_menu(request.user, store)
#     request.session['current_menu'] = menu
#     logger.debug('calling store.views.unapproved_agent_profile()')
#         
#     requestContext = RequestContext(request, {'menu':menu,
#                                               'store':store,
#                                               'user': request.user, 
#                                               'page_title': 'Unapproved agent profile'} )
# 
#     return render_to_response('unapproved-agent-profile.html', requestContext)
# 
# @login_required
# def agent_profile(request):
#     """
#     Default view show list of customers, order button for customer.
#     TODO: show store statistics: 
#     1.number of customers
#     2.number of orders
#     3.total profits
#     4.return ratio
#     """
#     
#     # list all customer of this agent
#     user = request.user
#     store_id = request.session['current_store_id']
#     store = Store.objects.get(id = store_id)
#     
#     customers = Customer.objects.filter(agent_id = user.id,store_id = store_id)
#     
#     # compute the menu
#     menu = MenuService.sales_menu(request.user, store)    
#     request.session['current_menu'] = menu
#     logger.debug('calling store.views.agent_profile()')
#         
#     requestContext = RequestContext(request, {'menu':menu,
#                                               'customers': customers,
#                                               'store':store,
#                                               'user': request.user, 
#                                               'page_title': 'Agent profile'} )
# 
#     return render_to_response('agent-profile.html', requestContext)
# 
# @login_required
# #@permission_required('store.enlist')
# def store_list(request, user_id):
#     """
#     Verify user has the access to enlist store.
#     """
#     logger.debug('calling store.views.store_list()')
#     user_name = request.user.username
#     
#     menu = MenuService.new_user_menu(request.user)
#     context = {
#         'menu':menu,
#         'page_title': 'Profile',
#         'user_name': user_name,
#     }
#     return render_to_response('profile.html', context)
# 
# 
# @login_required
# #@permission_required('store.edit')
# def store_edit(request, user_id, store_id):
#     logger.debug('calling store.views.store_list()')
# 
# 
# 
# class ProfileViewHelper:
#     """
#     Helper class to check user status and direct the view names
#     """
#     def __init__(self, user):
#         self._user = user
#     
#     
#     def direct_view(self, request):
#         """direct view
#         
#         return a dict for profile to process {'view_url': m, 'template':t ,'store_id': s }
#         
#         directly call view method
#         
#         sessions:
#         fav_color = request.session['fav_color']
#         request.session['has_commented'] = True
#         del request.session['member_id']
#         
#         """
# 
#         owned_store = self.get_owned_stores()
#         joined_store = self.get_joined_stores()
#         if owned_store:
#             # view owner_profile
#             request.session['current_store_id'] = owned_store.id
#              
#             return owner_profile(request)
#          
#         if joined_store:
#             # view sales_profile
#              
#             request.session['current_store_id'] = joined_store.id
#              
#             if self.is_approved_agent(joined_store.id):
#                 return agent_profile(request)
#             else:
#                 return unapproved_agent_profile(request)
#          
#  
#         return profile(request)
# 
#         # for version one, we allow owner login only
# #         groups = self._user.groups.values_list('name',flat=True)
# #         if 'Owner' in groups:
# #             owned_store = self.get_owned_stores()
# #             request.session['current_store_id'] = owned_store.id
# #             return owner_profile(request)
#         
#     def is_owner(self):
#         """ check if the user own stores, return true if user own store"""
#         return True
#         
#     def is_approved_agent(self, store_id):
#         """ check if the agent is approved by owner"""
#         enrollments = StoreEnrollment.objects.filter(store_id = store_id, agent_id=self._user.id, active=True)
#         if enrollments:
#             return True
#         else:
#             return False
#         
#     def get_owned_stores(self):
#         """ fetch list of stores a user owned"""
#         user_id = self._user.id
#         stores = Store.objects.filter(owner__id=user_id)
#         if stores:
#             return stores[0]
#         else:
#             return None
# 
#     def get_joined_stores(self):
#         """ fetch list of stores a user joined"""
#         user_id = self._user.id
#         stores = Store.objects.filter(sales__id=user_id)
#         if stores:
#             return stores[0]
#         else:
#             return None
#         
# @login_required
# def add_customer(request, store_id):
#     """
#     agent can add user after login.
#     
#     method assumes user is already approved. 
#     """
#     user = request.user
#     
#     if request.method == 'POST':
#         profile_form = UserProfileForm(data=request.POST)
#         if profile_form.is_valid():
#             user_profile = profile_form.save(commit=False)
#             user_profile.user=user
#             user_profile.save()
#             return store.views.profile(request) 
#         else:
#             print profile_form.errors
# #             return HttpResponse("Edit profile is failed.")
#             raise Http404("Edit profile is failed.")
#     else:
#         # for visitor, generate empty menu
#         menu = MenuService.visitor_menu()
#         profile_form = UserProfileForm()
#     requestContext = RequestContext(request, {'menu':menu,
#                                               'page_title': 'Edit Profile',
#                                               'profile_form': profile_form} )