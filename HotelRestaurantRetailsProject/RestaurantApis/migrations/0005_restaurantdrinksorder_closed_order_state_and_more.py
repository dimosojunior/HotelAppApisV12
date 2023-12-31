# Generated by Django 4.2.6 on 2023-10-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApis', '0004_restaurantdrinksorder_table_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantdrinksorder',
            name='closed_order_state',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Order Closed ?'),
        ),
        migrations.AddField(
            model_name='restaurantfoodorder',
            name='closed_order_state',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Order Closed ?'),
        ),
    ]
