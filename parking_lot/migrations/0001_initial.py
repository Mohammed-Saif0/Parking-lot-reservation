# Generated by Django 4.1.1 on 2022-09-20 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('is_cancled', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Parkinglots',
            fields=[
                ('parking_lot_id', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_spaces', models.IntegerField()),
                ('parking_lot_address', models.TextField(default='', max_length=200)),
                ('parking_lot_zipcode', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Parkingspaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_lot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_lot.parkinglots')),
            ],
        ),
        migrations.CreateModel(
            name='Cancel_booking',
            fields=[
                ('cancel_id', models.AutoField(primary_key=True, serialize=False)),
                ('reason', models.TextField(default='Empty', max_length=1000)),
                ('cancellation_date_time', models.DateTimeField(auto_now_add=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_lot.book_parking')),
            ],
        ),
        migrations.AddField(
            model_name='book_parking',
            name='parking_lot_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_lot.parkinglots'),
        ),
        migrations.AddField(
            model_name='book_parking',
            name='parking_space_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_lot.parkingspaces'),
        ),
        migrations.AddField(
            model_name='book_parking',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book_parking',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.vehicle'),
        ),
    ]
