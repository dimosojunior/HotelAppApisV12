# Generated by Django 4.2.6 on 2023-10-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApis', '0008_remove_hoteldrinksorder_orderitems_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelfoodorder',
            name='pending_total_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Pending Total Price'),
        ),
        migrations.AddField(
            model_name='hotelfoodorder',
            name='room_number',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Room Number'),
        ),
        migrations.AddField(
            model_name='hotelfoodorder',
            name='table_number',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Table Number'),
        ),
        migrations.AddField(
            model_name='hotelfoodorder',
            name='true_total_price',
            field=models.FloatField(blank=True, null=True, verbose_name='True Total Price'),
        ),
        migrations.AlterModelTable(
            name='hotelfoodorder',
            table=None,
        ),
    ]