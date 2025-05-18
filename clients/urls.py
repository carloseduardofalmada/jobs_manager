from django.urls import path
from .views import (
    ClientListView,
    ClientUpdateView,
    ClientCreateView,
    UnusedClientsView
)

app_name = 'clients'

urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('<uuid:pk>/', ClientUpdateView.as_view(), name='update'),
    path('add/', ClientCreateView.as_view(), name='create'),
    path('unused/', UnusedClientsView.as_view(), name='unused'),
]