# Generated by Django 5.0.4 on 2024-04-22 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_etazh_edinica_kabinet_edinica_lico_edinica_remont_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='edinica',
            name='mac',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='MAC-адрес'),
        ),
    ]