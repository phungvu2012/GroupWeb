from django.urls import path

from . import views

urlpatterns = [
    path('', views.grouplist, name='groupapp'),
    path('<int:id>/', views.detailGroup),
]