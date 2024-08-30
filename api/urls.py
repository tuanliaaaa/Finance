from django.urls import path
from .views import Login,Humen,Finances
urlpatterns = [
    path('login',Login.as_view()),
    path('humen',Humen.as_view()),
    path('finances',Finances.as_view())

]
