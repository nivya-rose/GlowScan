from django.urls import path
from . import views
from .models import Profile

urlpatterns=[
    path('', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('start_scan/', views.start_scan, name='start_scan'),
    path('account/',views.user_account,name='user_account'),
    path('start_scan/', views.start_scan, name='start_scan'),
   
]



