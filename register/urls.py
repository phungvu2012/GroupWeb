from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.loginAndRegister, name='register'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/login'),name='logout'),
]