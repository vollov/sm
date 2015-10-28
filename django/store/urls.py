from django.conf.urls import url

from store import views

urlpatterns = [

    url(r'^products/$', views.products, name='products'),
    
#     url(r'^show/(?P<mid>\S+)/$', views.show_msg, name='show_msg'),
]