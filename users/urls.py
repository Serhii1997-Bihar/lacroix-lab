from django.urls import path
from users.views import *

urlpatterns = [
    path('creation/', create_user, name='create_user'),
    path('login/', user_login, name='user_login'),
    path('dashboard/<int:user_id>/', user_dashboard, name='user_dashboard'),
    path('edit/', edit_data, name='edit_data'),
    path('logout/', user_logout, name='user_logout'),
    path('accounts/', users_list, name='users_list'),
    path('profile/<int:user_id>/', user_profile, name='user_profile'),
    path('message/<int:user_id>/', send_message, name='send_message'),
    path('message_in/', message_in, name='message_in'),
    path('dialogue/<int:user_id>/', dialogue, name='dialogue'),
    path('delete_image/<int:user_id>/', delete_image, name='delete_image'),
    path('delete_video/<int:user_id>/', delete_video, name='delete_video'),
]
