from django.urls import path
from django.conf.urls import url
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
]