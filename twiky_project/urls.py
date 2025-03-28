"""
URL configuration for twiky_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView  # ✅ Import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ✅ Redirect root URL `/` to `/twicky/`
    path('', RedirectView.as_view(url='/twicky/', permanent=True)),

    # ✅ Include your app URLs
    path('twicky/', include('twicky.urls')),
    path('account/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
