# Generated by Django 5.0.4 on 2024-04-22 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0012_alter_edinica_etazh_alter_edinica_kabinet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edinica',
            name='etazh',
            field=models.ForeignKey(blank=True, default=None, max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='storage.etazh', verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='edinica',
            name='kabinet',
            field=models.ForeignKey(blank=True, default=None, max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='storage.kabinet', verbose_name='Кабинет'),
        ),
    ]