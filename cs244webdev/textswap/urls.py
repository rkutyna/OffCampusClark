from django.urls import path
from .views import *

urlpatterns = [
    path('', my_home_view, name='home'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('messages/',message_view, name = 'messages')
    # Add other URLs as needed
]