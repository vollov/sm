from django.conf.urls import patterns, url

from account import views
import sales.views

urlpatterns = patterns('',

    # ex: /account/register/
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.sign_in, name='sign_in'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^customer/new/$', sales.views.customer_form, name='customer_form'),
    url(r'^customer/save/$', sales.views.save_customer, name='save_customer'),
    url(r'^customers/$', sales.views.customers, name='customers'),
    url(r'^orders/$', sales.views.orders, name='orders'),
    url(r'^order/(?P<order_id>\S+)/$', sales.views.order_detail, name='order_detail'),
#     url(r'^vehicle/(?P<oid>\S+)/$', views.vehicle, name='vehicle'),
    
)