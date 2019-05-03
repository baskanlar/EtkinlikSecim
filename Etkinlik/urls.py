from django.urls import path
from .views import *

app_name = 'etlinlik'
urlpatterns = [
    path('', home_view, name='home'),
    path('api_create', mail_create_api),
    path('etkinlik_all', Etkinlik_all),
]
