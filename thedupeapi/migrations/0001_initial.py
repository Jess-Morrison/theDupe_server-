# Generated by Django 4.2.2 on 2023-07-26 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=55)),
                ('country', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('first_name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=55)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedupeapi.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedupeapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedupeapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Dupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dupe_name', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=55)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedupeapi.company')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedupeapi.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedupeapi.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedupeapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='CheckoutSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_details', models.CharField(max_length=55)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('completed_at', models.DateTimeField(auto_now=True)),
                ('active_status', models.BooleanField()),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='thedupeapi.order')),
                ('payment_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedupeapi.paymenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedupeapi.user')),
            ],
        ),
    ]
