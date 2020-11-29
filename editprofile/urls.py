from django.urls import path

from . import views

urlpatterns = [
    path('', views.edit, name='edit'),
    path('changepassword', views.change_password, name='changepassword'),
    path('changeavatar', views.change_avatar, name='changeavatar'),
    # url(r'^password/$', views.change_password, name='change_password'),
]