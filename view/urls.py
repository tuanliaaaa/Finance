from django.urls import path
from .views import ok
urlpatterns = [
    path('login',ok.as_view()),
]
