from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from ..models import Client
from ..forms import ClientForm

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('clients:list')

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('clients:list')

class UnusedClientsView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/unused_clients.html'
    context_object_name = 'unused_clients'

    def get_queryset(self):
        return Client.objects.filter(job__isnull=True)

def all_clients(request):
    clients = Client.objects.all().values('id', 'name')
    return JsonResponse(list(clients), safe=False)