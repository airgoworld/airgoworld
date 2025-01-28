# Generated by Django 5.1.5 on 2025-01-27 03:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('suite', 'Suite'), ('penthouse', 'Penthouse')], default='single', max_length=20)),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available', max_length=20)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img', models.ImageField(blank=True, null=True, upload_to='rooms/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('bed', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotel.hotel')),
            ],
        ),
    ]
