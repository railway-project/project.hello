"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from myproject.views import contactus, aboutus, tailwind
from poems.views import home, search, poem_detail, post_detail, view_system
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import urls as auth_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/password-reset/', include(auth_urls)),
    path('', home, name='home'),
    path('poem/<slug:slug>/<int:pk>/', poem_detail, name='poem-detail'),
    path('contact-us/', contactus, name='contactus'),
    path('about-us/', aboutus, name='aboutus'),
    path('tailwind/', tailwind, name='tail'),
    path('search_result/', search, name='search'),
    path('post/<int:pk>/<slug:slug>/', post_detail, name='post_detail'),
    path('poem/<slug:slug>/<int:pk>/', view_system, name='view_system'),
    re_path(r'^.*/$', home, name='home'),
    re_path(r'^.*$', home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
