from django.contrib import admin
from django.urls import path
from auths.views import LoginAPIView, RegisterAPIView

app_name='auths'

urlpatterns = [
    path('login', LoginAPIView.as_view()),
    path('registration', RegisterAPIView.as_view()),
]