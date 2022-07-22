from django.urls import path

from . import views


app_name = 'api'
urlpatterns = [
    path('google', views.google, name='google'),
]
