from django.conf.urls import url

from store import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^owner/$', views.owner_profile, name='owner_profile'),
    url(r'^agent/$', views.agent_profile, name='agent_profile'),
    url(r'^unapproved-agent/$', views.unapproved_agent_profile, name='unapproved_agent_profile'),
    
    url(r'^new/$', views.create_store, name='create_store'),
#     url(r'^show/(?P<mid>\S+)/$', views.show_msg, name='show_msg'),
]