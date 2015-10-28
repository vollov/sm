from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import index as home

urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'^store/', include('store.urls')),
#     url(r'^sales/', include('sales.urls')),
#     url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
#     url(r'^captcha/', include('captcha.urls')),
]


# settings for development environment DEBUG
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
