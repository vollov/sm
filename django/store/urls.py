from django.conf.urls import url

from store import views

urlpatterns = [
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^orders/$', views.orders, name='orders'),
    url(r'^order/(?P<order_id>\S+)/$', views.order_detail, name='order_detail'),
    url(r'^products/$', views.products, name='products'),
    url(r'^product/(?P<sku>\S+)/$', views.product_detail, name='product_detail'),
#     url(r'^show/(?P<mid>\S+)/$', views.show_msg, name='show_msg'),
]