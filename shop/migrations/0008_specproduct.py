# Generated by Django 3.2.4 on 2021-08-13 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('microcontroller', models.CharField(max_length=20)),
                ('operating_voltage', models.CharField(max_length=10)),
                ('input_voltage_recomended', models.CharField(max_length=10)),
                ('input_voltage_limit', models.CharField(max_length=10)),
                ('IO_pins', models.IntegerField()),
                ('pwm_IO_pins', models.IntegerField()),
                ('dc_current_per_IO_pin', models.IntegerField()),
                ('dc_current_for_3_3v_pin', models.IntegerField()),
                ('flash_memory', models.CharField(max_length=50)),
                ('sram', models.CharField(max_length=20)),
                ('eeprom', models.CharField(max_length=20)),
                ('clock_speed', models.IntegerField()),
                ('led_builtin', models.IntegerField()),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]