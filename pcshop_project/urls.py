from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.urls.conf import re_path
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('shop.urls')),
    path('search/', include('search_app.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('vouchers/', include('vouchers.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
