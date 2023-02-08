from . import views
from django.urls import path

urlpatterns = [
    path('', views.booking, name="booking"),
    path('edit-booking', views.enter_ref, name='enter_ref'),
]
