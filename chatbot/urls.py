from django.urls import path
from . import views

# urls.py (app level)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/login/', views.user_login, name='login'),
    path('api/chat/', views.chat, name='chat'),
    path('api/history/', views.get_chat_history, name='history'),
]