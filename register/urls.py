from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('',auth_views.LoginView.as_view(template_name="pages/register.html"), name="login"),
    path('', views.register, name='register'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/register'),name='logout'),
]