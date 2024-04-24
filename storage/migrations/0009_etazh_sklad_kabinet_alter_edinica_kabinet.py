# Generated by Django 5.0.4 on 2024-04-22 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0008_remove_edinica_id_edinica_invent'),
    ]

    operations = [
        migrations.AddField(
            model_name='etazh',
            name='sklad',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='storage.sklads', verbose_name='Склад'),
        ),
        migrations.CreateModel(
            name='Kabinet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Номер кабинета')),
                ('etazh', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='storage.etazh', verbose_name='Этаж')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинеты',
            },
        ),
        migrations.AlterField(
            model_name='edinica',
            name='kabinet',
            field=models.ForeignKey(blank=True, default=None, max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='storage.kabinet', verbose_name='Кабинет'),
        ),
    ]