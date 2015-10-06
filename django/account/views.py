from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Rango says hey there world!")

from account.forms import UserForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from store.service import MenuService

def register(request):

#     registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            human = True
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

#             registered = True
            return store.views.profile(request)
#             return HttpResponseRedirect('/store/profile')
        else:
            print user_form.errors
            return HttpResponse("Your registration is failed.")
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        # for visitor, generate empty menu
        menu = MenuService.visitor_menu()
        
        user_form = UserForm()
        
    requestContext = RequestContext(request, {'menu':menu,
                                              'user_form': user_form, 
                                              'page_title': 'Register',
                                              'registered': registered} )

    # Render the template depending on the context.
    return render_to_response('register.html', requestContext)
    
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def sign_in(request):
    logger.debug('enter sign_in() {0}'.format(request))
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the email/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                logger.debug('user active, login() {0}, {1}'.format(request, user))
                login(request, user)
                return HttpResponseRedirect('/store/profile/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(email, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # for visitor, generate empty menu
        menu = MenuService.visitor_menu()
        
        requestContext = RequestContext(request, {'menu':menu,
                                                  'page_title': 'Login'} )
         
        return render_to_response('login.html', requestContext)
    
from django.contrib.auth import logout

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logger.debug('user_logout() {0}'.format(request))
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/account/login')