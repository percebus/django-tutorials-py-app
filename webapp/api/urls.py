from django.urls import path

from . import views


app_name = 'api'
urlpatterns = [
    path('OK/', views.OK, name='OK'),
    path('found/not/', views.not_found, name='not_found'),

    path('teapot/', views.teapot, name='teapot'),

    path('google/', views.google, name='google')
]
