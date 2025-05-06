from django.urls import path
from .views import home, login, chat
from .views import index, profile, settings

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('settings/', settings, name='settings'),
    path('chat/', chat, name='chat'),
]
