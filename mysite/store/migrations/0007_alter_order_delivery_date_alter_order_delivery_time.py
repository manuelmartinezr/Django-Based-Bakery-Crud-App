# Generated by Django 5.0.6 on 2024-06-04 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_deliveryvehicle_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]