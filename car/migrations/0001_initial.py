# Generated by Django 5.1.5 on 2025-01-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=20)),
                ('car_type', models.CharField(choices=[('SUV', 'SUV'), ('Sedan', 'Sedan'), ('Truck', 'Truck'), ('Hatchback', 'Hatchback'), ('Coupe', 'Coupe')], max_length=20)),
                ('rental_price', models.IntegerField(default=0)),
                ('speed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('images', models.JSONField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('display', models.BooleanField(default=True)),
                ('fuel_type', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('capacity', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
