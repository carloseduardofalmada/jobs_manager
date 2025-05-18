from django.urls import path
from .views import client_view  # Adicionar import correto

app_name = 'clients'

urlpatterns = [
    path('', client_view.ClientListView.as_view(), name='list'),
    path('<uuid:pk>/', client_view.ClientUpdateView.as_view(), name='update'),
    path('add/', client_view.ClientCreateView.as_view(), name='create'),
    path("api/clients/all/", client_view.all_clients, name="all_clients_api"),
]