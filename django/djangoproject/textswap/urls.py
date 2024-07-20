from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', my_home_view, name='home'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('messages/', inbox, name = 'messages'),
    path('filtered_apartments/', filtered_apartments, name='filtered_apartments'),
    path('create/', create_apartment_view, name='create_apartment'),
    path('apartment/<int:pk>/', apartment_detail_view, name='apartment_detail'),
    path('user_listings/', user_listings_view, name='user_listings'),
    path('edit_apartment/<int:apartment_id>/', edit_apartment, name='edit_apartment'),
    path('logout/', logout_view, name='logout'),
    path('delete_apartment/<int:apartment_id>/', delete_apartment, name='delete_apartment'),
    
    path('inbox/', inbox, name='inbox'),
    path('api/get_latest_message/<str:sender_username>/', get_latest_message, name='get_latest_message'),
    path('message/<int:message_id>/', read_message, name='read_message'),
    path('messaging/<str:username>/', send_message, name='send_message'),
    path('mark_messages_as_read/<str:recipient_username>/', mark_messages_as_read, name='mark_messages_as_read'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)