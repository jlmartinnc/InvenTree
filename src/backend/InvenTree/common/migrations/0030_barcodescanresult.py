# Generated by Django 4.2.15 on 2024-09-21 06:05

import InvenTree.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0029_inventreecustomuserstatemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarcodeScanResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(help_text='Barcode data', max_length=250, verbose_name='Data')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='Date and time of the barcode scan', verbose_name='Timestamp')),
                ('endpoint', models.CharField(blank=True, help_text='URL endpoint which processed the barcode', max_length=250, null=True, verbose_name='Path')),
                ('context', models.JSONField(blank=True, help_text='Context data for the barcode scan', max_length=1000, null=True, verbose_name='Context')),
                ('response', models.JSONField(blank=True, help_text='Response data from the barcode scan', max_length=1000, null=True, verbose_name='Response')),
                ('result', models.BooleanField(default=False, help_text='Was the barcode scan successful?', verbose_name='Result')),
                ('user', models.ForeignKey(blank=True, help_text='User who scanned the barcode', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Barcode Scan',
            },
            bases=(InvenTree.models.PluginValidationMixin, models.Model),
        ),
    ]
