# Generated by Django 4.2.6 on 2023-10-27 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApis', '0002_alter_restaurantdrinksorder_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restauranttables',
            name='TableStatus',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Table Status'),
        ),
    ]
