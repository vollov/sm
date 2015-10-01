from django.conf.urls import url

from store import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
#     url(r'^show/(?P<mid>\S+)/$', views.show_msg, name='show_msg'),
]