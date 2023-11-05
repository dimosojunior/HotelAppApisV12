# Generated by Django 4.2.6 on 2023-10-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApis', '0012_remove_hoteldrinksorderitems_is_customer_closed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoteldrinksorder',
            name='closed_order_state',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Order Closed ?'),
        ),
        migrations.AddField(
            model_name='hotelfoodorder',
            name='closed_order_state',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Order Closed ?'),
        ),
        migrations.AddField(
            model_name='hotelroomsorder',
            name='closed_order_state',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Order Closed ?'),
        ),
    ]