from django.urls import path
from .views import *

app_name = 'etlinlik'

urlpatterns = [
    path('', home_view, name='home'),
    path('etkinlik_all', etkinlik_all),
    path('etkinlik_mail', etkinlik_mail),
]
