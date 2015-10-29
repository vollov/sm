


# from django.shortcuts import render, redirect
# 
# from .forms import CustomerForm
# from .models import Customer, Order, ProductOrder, Product
# from store.models import Store
# 
# import logging
# logger = logging.getLogger(__name__)
# 
# from django.contrib.auth.decorators import login_required
# from django.template import RequestContext
# from django.shortcuts import render_to_response, get_object_or_404
# 
# 


# @login_required
# def customers(request):
#     """
#     agent list customers
#     """
#     user = request.user
#     store_id = request.session['current_store_id']
#     store = Store.objects.get(id = store_id)
#     menu = request.session['current_menu']
#     customers = Customer.objects.filter(agent_id=user.id, store_id=store.id)
#     
#     requestContext = RequestContext(request, {'menu':menu,
#                                               'customers': customers,
#                                               'user':user,
#                                               'store':store,
#                                               'page_title': 'Customers'} )
#          
#     return render_to_response('customers.html', requestContext)
# 
#     
# 
# @login_required
# def customer_form(request):
#     """
#     agent pull customer form
#     """
#     user = request.user
#     store_id = request.session['current_store_id']
#     store = Store.objects.get(id = store_id)
#     menu = request.session['current_menu']
#     
#     customer_form = CustomerForm()
#     requestContext = RequestContext(request, {'menu':menu,
#                                               'page_title': 'Edit Profile',
#                                               'customer_form': customer_form} )
#     
#     return render_to_response('customer-form.html', requestContext)
#     
# @login_required
# def save_customer(request):
#     """
#     agent save customer
#     """
#     if request.method == 'POST':
#         user = request.user
#         store_id = request.session['current_store_id']
#         store = Store.objects.get(id = store_id)
#     
#         customer_form = CustomerForm(data=request.POST)
#         if customer_form.is_valid():
#             customer = customer_form.save(commit=False)
#             customer.agent = user
#             customer.store = store
#             customer.save()
#             
#             # redirect to customer list page 
#             return customers(request) 
#         else:
#             print customer_form.errors
# #             return HttpResponse("Edit profile is failed.")
#             raise Http404("Edit customer is failed.")
#     else:
#         logger.error('Can not save customer via HTTP get.')
#         raise Http404('Can not save customer via HTTP get.')

