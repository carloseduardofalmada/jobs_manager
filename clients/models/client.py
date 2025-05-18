import uuid
from django.db import models

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    xero_contact_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_account_customer = models.BooleanField(default=False)
    raw_json = models.JSONField(blank=True, null=True)
    xero_last_modified = models.DateTimeField(null=True)
    xero_last_synced = models.DateTimeField(null=True)
    django_created_at = models.DateTimeField(auto_now_add=True)
    django_updated_at = models.DateTimeField(auto_now=True)
    xero_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'clients_client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name