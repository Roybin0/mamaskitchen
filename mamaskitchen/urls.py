"""mamaskitchen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from bookings import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path('booking/', include("bookings.urls"), name='booking'),
    path('edit-booking', views.enter_ref_edit, name='enter_ref_edit'),
    path('edit-booking/<booking_ref>',
         views.edit_booking, name='edit-booking'),
    path('cancel-booking', views.enter_ref_delete, name='enter_ref_delete'),
    path('cancel-booking/<booking_ref>', views.delete_booking, name='cancel'),
    path('cancelled', views.cancelled, name='cancelled'),
    path('thanks/', views.thankyou, name='thankyou'),
    path('menu', views.menu, name='menu'),
    path('privacy-policy', views.privacy, name='privacy'),
    path('contact', views.contact, name='contact'),
    path('accounts/', include('allauth.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
