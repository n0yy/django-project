# Generated by Django 3.2.4 on 2021-08-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_specproduct_analog_pins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specproduct',
            name='flash_memory',
            field=models.CharField(max_length=100),
        ),
    ]