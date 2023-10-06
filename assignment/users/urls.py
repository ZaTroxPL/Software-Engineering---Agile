from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit_profile/', views.UserChangeView.as_view(), name='edit_profile')
]