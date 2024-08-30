from django.urls import path
from .views import L
urlpatterns = [
    path('login',L.as_view())
]
