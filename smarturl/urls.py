from django.conf.urls import url
from django.contrib import admin
from main.views import index, get_url
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^(\w+)/$', get_url)
]


if not settings.DEBUG:
    urlpatterns += [url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})]

# urlpatterns += [url(r'^([\w/]+)', get_url)]
