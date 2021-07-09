from django.urls import path
from .views import create_post, create_user

urlpatterns = [
    path('', create_post),
    path('user/', create_user)
]