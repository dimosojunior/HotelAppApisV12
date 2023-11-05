# Generated by Django 4.2.6 on 2023-10-26 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApis', '0007_alter_hoteldrinksorder_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoteldrinksorder',
            name='orderItems',
        ),
        migrations.RemoveField(
            model_name='hotelfoodorder',
            name='orderItems',
        ),
        migrations.RemoveField(
            model_name='hotelroomsorder',
            name='orderItems',
        ),
        migrations.AddField(
            model_name='hoteldrinksorder',
            name='items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HotelApis.hoteldrinksorderitems'),
        ),
        migrations.AddField(
            model_name='hoteldrinksorderitems',
            name='is_customer_closed',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Customer Closed Status'),
        ),
        migrations.AddField(
            model_name='hoteldrinksorderitems',
            name='is_customer_opened',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Customer Opened Status'),
        ),
        migrations.AddField(
            model_name='hotelfoodorder',
            name='items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HotelApis.hotelfoodorderitems'),
        ),
        migrations.AddField(
            model_name='hotelfoodorderitems',
            name='is_customer_closed',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Customer Closed Status'),
        ),
        migrations.AddField(
            model_name='hotelfoodorderitems',
            name='is_customer_opened',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Customer Opened Status'),
        ),
        migrations.AddField(
            model_name='hotelroomsorder',
            name='items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HotelApis.hotelroomsorderitems'),
        ),
        migrations.AddField(
            model_name='hotelroomsorderitems',
            name='is_customer_closed',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Customer Closed Status'),
        ),
        migrations.AddField(
            model_name='hotelroomsorderitems',
            name='is_customer_opened',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Customer Opened Status'),
        ),
    ]
