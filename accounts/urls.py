from django.urls import path

from accounts.views import login_view, logout_view, signin_view

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='accounts/login'),
    path('logout/', logout_view, name='accounts/logout_view'),
    path('signin/', signin_view, name='accounts/signin_view'),
   
]