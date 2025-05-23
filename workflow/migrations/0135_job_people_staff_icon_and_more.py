# Generated by Django 5.2 on 2025-05-07 00:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("workflow", "0134_alter_purchaseorder_order_date")]

    operations = [
        migrations.AddField(
            model_name="job",
            name="people",
            field=models.ManyToManyField(
                related_name="assigned_jobs", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="staff",
            name="icon",
            field=models.ImageField(blank=True, null=True, upload_to="staff_icons/"),
        ),
        migrations.AddField(
            model_name="historicalstaff",
            name="icon",
            field=models.ImageField(blank=True, null=True, upload_to="staff_icons/")
        )
    ]
