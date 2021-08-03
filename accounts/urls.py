
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('accounts', views.accounts, name='accounts'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('profile/',views.profile,name='profile'), # p2c-21-105
    path('register/',views.register,name='register'),
    path('email_verify/',views.email_verify,name='email_verify'),
    path('otp/',views.otp,name='otp'),
    path('linked_in/',views.linked_in,name='linked_in'),
    path('otp_password/',views.otp_password,name='otp_password'),
    path('new_password/',views.new_password,name='new_password'),
    
]