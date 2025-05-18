from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'is_account_customer')
    list_filter = ('is_account_customer',)
    search_fields = ('name', 'email', 'phone')
    ordering = ('name',)