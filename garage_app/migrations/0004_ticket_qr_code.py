# Generated by Django 3.2.9 on 2021-12-03 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_app', '0003_alter_ticket_position_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='qr_code',
            field=models.TextField(default='hello', verbose_name='رمز رابط التذكرة'),
        ),
    ]
