from . import views
from django.urls import path

urlpatterns = [
    path('', views.booking, name="booking"),
    path('edit-booking', views.enter_ref_edit, name='enter_ref_edit'),
    path('cancel-booking', views.enter_ref_delete, name='enter_ref_delete'),
]
