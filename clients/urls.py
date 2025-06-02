from django.urls import path
from .views import client_view

app_name = 'clients'

urlpatterns = [
    # Regular views
    path('', client_view.ClientListView.as_view(), name='list'),
    path('<uuid:pk>/', client_view.ClientUpdateView.as_view(), name='update'),
    path('add/', client_view.AddClient, name='create'),
    path('unused/', client_view.UnusedClientsView.as_view(), name='unused'),
    
    # API endpoints
    path('api/all/', client_view.all_clients, name='api_all'),
    path('api/search/', client_view.ClientSearch, name='api_search'),
    path('api/detail/', client_view.client_detail, name='api_detail'),
]
