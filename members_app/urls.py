from django.urls import path
from .views import input_page, display_page, session_page, clear_session

urlpatterns = [
    path('input/', input_page, name='input_page'),
    path('display/', display_page, name='display_page'),
    path('session/', session_page, name='session_page'),
    path('clear_session/', clear_session, name='clear_session'),
]