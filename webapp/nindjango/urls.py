from django.urls import path
from .api import api

app_name = 'nindjango'
urlpatterns = [
    path("", api.urls),
]
