from django.urls import path

from . import views


app_name = 'cds-hooks'
urlpatterns = [
    path('patient-greeting', views.patient_greeting, name='patient-greeting'),

    path('aggregated/patient-view', views.patient_view, name='patient-view'),
    path('aggregated/order-select', views.order_select, name='order-select')
]
