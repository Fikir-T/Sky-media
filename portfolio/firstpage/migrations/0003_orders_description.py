# Generated by Django 5.2 on 2025-04-03 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstpage', '0002_orders_customer_email_alter_orders_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
    ]
