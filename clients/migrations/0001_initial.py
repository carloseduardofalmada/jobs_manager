from django.db import migrations, models
import uuid

class Migration(migrations.Migration):
    initial = True
    
    dependencies = []

    state_operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, null=True)),
                ('phone', models.CharField(max_length=50, blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('is_account_customer', models.BooleanField(default=False)),
                ('xero_contact_id', models.CharField(max_length=255, unique=True)),
                ('raw_json', models.JSONField(blank=True, null=True)),
                ('xero_last_modified', models.DateTimeField(null=True)),
                ('xero_last_synced', models.DateTimeField(null=True)),
                ('django_created_at', models.DateTimeField(auto_now_add=True)),
                ('django_updated_at', models.DateTimeField(auto_now=True)),
                ('xero_tenant_id', models.CharField(max_length=255, blank=True, null=True)),
            ],
            options={
                'db_table': 'workflow_client',
            },
        ),
    ]

    database_operations = []

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations
        )
    ]