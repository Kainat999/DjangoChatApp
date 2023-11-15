from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import index, landing_page_view, register, chat_rooms_static_view

urlpatterns = [
    path('', landing_page_view, name='landing_page'),
    path('chat/', chat_rooms_static_view, name='chatroom'),
    path('<str:group_name>/', index, name='home'),
    path('accounts/register/', register, name='registration'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]

