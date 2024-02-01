from django.urls import path
from .views import login_view, registration_view,my_home_view

urlpatterns = [
    path('', my_home_view, name='home'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration')
    # Add other URLs as needed
]