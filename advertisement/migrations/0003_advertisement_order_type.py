# Generated by Django 2.1.5 on 2019-01-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_advertisement_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='order_type',
            field=models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], default='sell', max_length=4),
        ),
    ]
