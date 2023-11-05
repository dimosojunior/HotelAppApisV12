# Generated by Django 4.2.6 on 2023-10-28 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HotelApis', '0014_hotelotherscart_hotelotherscategories_and_more'),
        ('RetailsApis', '0005_retailsdrinksorder_closed_order_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetailsOthersCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('total_price', models.FloatField(default=0, verbose_name='Total Price')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Retails Others Cart',
            },
        ),
        migrations.CreateModel(
            name='RetailsOthersOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(verbose_name='Total Price')),
                ('closed_order_state', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Order Closed ?')),
                ('table_number', models.CharField(blank=True, max_length=500, null=True, verbose_name='Table Number')),
                ('order_status', models.BooleanField(blank=True, default=False, null=True, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RetailsApis.retailsotherscart')),
            ],
            options={
                'verbose_name_plural': 'Retails Others Orders',
            },
        ),
        migrations.CreateModel(
            name='RetailsOthersProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='Wali', max_length=100, verbose_name='Product Name')),
                ('product_second_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Product Second Name')),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('ProductQuantity', models.IntegerField(blank=True, null=True, verbose_name='Product Quantity')),
                ('InitialProductQuantity', models.IntegerField(blank=True, null=True, verbose_name='Initial Product Quantity')),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/RetailsInventoryImages/', verbose_name='Category Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('StoreBinCode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='RetailsApis.retailsstorebincode', verbose_name='Store Bin Code')),
                ('StoreCode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RetailsApis.retailsstorecode', verbose_name='Store Code')),
                ('Unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='RetailsApis.retailsproductsunit', verbose_name='Product Unit')),
                ('productCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HotelApis.retailsotherscategories', verbose_name='Product Category')),
            ],
            options={
                'verbose_name_plural': 'Retails Others Products',
            },
        ),
        migrations.CreateModel(
            name='RetailsOthersOrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('order_status', models.BooleanField(blank=True, default=False, null=True, verbose_name='Status')),
                ('quantity', models.IntegerField(default=1)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RetailsApis.retailscustomers')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RetailsApis.retailsothersorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RetailsApis.retailsothersproducts')),
                ('table', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='RetailsApis.retailstables')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Retails Others Orders Items',
            },
        ),
        migrations.AddField(
            model_name='retailsothersorder',
            name='orderItems',
            field=models.ManyToManyField(to='RetailsApis.retailsothersorderitems'),
        ),
        migrations.AddField(
            model_name='retailsothersorder',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='RetailsOthersCartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RetailsApis.retailsotherscart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RetailsApis.retailsothersproducts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Retails Others Cart Items',
            },
        ),
    ]
