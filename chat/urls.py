from django.urls import path
from chat import views 
from django.contrib.auth.views import LoginView, LogoutView
 
 
urlpatterns = [
    # path("", chat_views.chatPage, name="chat-page"),
 
    # login-section
    path("", views.room_list, name='chat-list'),
    path("<str:room_name>/", views.room_view, name='chat-room'),
]