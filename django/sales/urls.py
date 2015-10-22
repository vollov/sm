from django.conf.urls import patterns, url

from account import views

urlpatterns = patterns('',

    # ex: /account/register/
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.sign_in, name='sign_in'),
    url(r'^logout/$', views.user_logout, name='logout'),
#     url(r'^vehicle/(?P<oid>\S+)/$', views.vehicle, name='vehicle'),
    
)