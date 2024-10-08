# Generated by Django 5.1 on 2024-08-26 16:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReservationChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('number_of_adults', models.IntegerField()),
                ('number_of_children', models.IntegerField()),
                ('currency', models.CharField(max_length=3)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed')], default='PENDING', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='reservation_engine.guest')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='reservation_engine.property')),
            ],
        ),
        migrations.CreateModel(
            name='ChannelReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_reservation_id', models.CharField(max_length=100)),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='channel_reservation', to='reservation_engine.reservation')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation_engine.reservationchannel')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='reservation_engine.property')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='reservation_engine.room'),
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('description', models.TextField()),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_types', to='reservation_engine.property')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='reservation_engine.roomtype'),
        ),
    ]
