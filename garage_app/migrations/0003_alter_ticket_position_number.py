# Generated by Django 3.2.9 on 2021-11-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_app', '0002_auto_20211119_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='position_number',
            field=models.CharField(max_length=10, verbose_name='رقم حارة الركن'),
        ),
    ]
