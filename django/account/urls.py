from django.conf.urls import patterns, url

from account import views

urlpatterns = patterns('',

    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_form, name='login_form'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', views.user_logout, name='logout'),
#     url(r'^vehicle/(?P<oid>\S+)/$', views.vehicle, name='vehicle'),


)