from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', my_home_view, name='home'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('messages/',message_view, name = 'messages'),
    path('filtered_apartments/', filtered_apartments, name='filtered_apartments'),
    path('create/', create_apartment_view, name='create_apartment'),
    path('apartment/<int:pk>/', apartment_detail_view, name='apartment_detail'),
    path('user_listings/', user_listings_view, name='user_listings'),
    path('edit_apartment/<int:apartment_id>/', edit_apartment, name='edit_apartment'),
    path('logout/', logout_view, name='logout'),
    path('delete_apartment/<int:apartment_id>/', delete_apartment, name='delete_apartment'),
    # Add other URLs as needed
    
    path('create-message/', create_message, name='create-message'),
    path('stream-chat-messages/', stream_chat_messages, name='stream-chat-messages'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)