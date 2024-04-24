# Generated by Django 5.0.4 on 2024-04-22 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_edinica_mac'),
    ]

    operations = [
        migrations.AddField(
            model_name='etazh',
            name='sklad',
            field=models.ForeignKey(blank=True, default=None, max_length=10, null=True, on_delete=django.db.models.deletion.SET_NULL, to='storage.sklads', verbose_name='На каком складе'),
        ),
    ]
