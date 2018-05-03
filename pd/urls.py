from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'printer'

urlpatterns = [
    path('', views.login_view),
    path('home/', views.home_view),
    path('history/', views.history_view),
    path('vehicles/', views.vehicle_view),
    path('logout/', views.logout_view),
    ]