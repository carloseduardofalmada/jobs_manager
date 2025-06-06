# Generated by Django 5.1.5 on 2025-03-04 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workflow", "0085_auto_20250302_2205"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicaljob",
            name="contact_person",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="contact_person",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="xerotoken",
            name="scope",
            field=models.TextField(
                default="offline_access openid profile email accounting.contacts accounting.transactions accounting.reports.read accounting.settings accounting.journals.read"
            ),
        ),
    ]
