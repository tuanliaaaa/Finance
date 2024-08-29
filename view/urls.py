from django.urls import path
from .views import Login,L
urlpatterns = [
    path('login',Login.as_view()),
    path('logina',L.as_view())
]
