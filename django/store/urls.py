from django.conf.urls import url

from store import views

urlpatterns = [

    url(r'^new/$', views.create_store, name='create_store'),
#     url(r'^show/(?P<mid>\S+)/$', views.show_msg, name='show_msg'),
]