# Generated by Django 3.2.9 on 2021-11-14 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('national_identification_number', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ticket_total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parking_price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car_color', models.CharField(max_length=30)),
                ('car_owner_name', models.CharField(max_length=30)),
                ('reservation_time_per_day', models.CharField(max_length=30)),
                ('owner_mobile_number', models.CharField(max_length=30)),
                ('car_model_name', models.CharField(max_length=30)),
                ('position_number', models.IntegerField(default=1)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('car_model_year', models.IntegerField()),
                ('car_registration_no', models.CharField(max_length=30)),
                ('driver_license_number', models.CharField(max_length=30)),
                ('car_plate', models.CharField(max_length=30)),
                ('car_manufacturer', models.CharField(max_length=30)),
                ('car_chassis_no', models.CharField(max_length=30)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]