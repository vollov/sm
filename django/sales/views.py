from django.shortcuts import render

from .forms import CustomerForm

@login_required
def customer_form(request):
    """
    agent can add customer
    """
    
    if request.method == 'POST':
        customer_form = CustomerForm(data=request.POST)
        if customer_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.user=user
            user_profile.save()
            return store.views.profile(request) 
        else:
            print profile_form.errors
#             return HttpResponse("Edit profile is failed.")
            raise Http404("Edit profile is failed.")
    else:
        # for 
        menu = MenuService.visitor_menu()
        profile_form = UserProfileForm()
    requestContext = RequestContext(request, {'menu':menu,
                                              'page_title': 'Edit Profile',
                                              'profile_form': profile_form} )
    
@login_required
def save_customer(request):

