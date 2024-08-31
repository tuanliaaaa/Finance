from django.urls import path
from .views import login,home
urlpatterns = [
    path('login',login.as_view()),
    path('home',home.as_view())
]
