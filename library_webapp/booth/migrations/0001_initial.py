# Generated by Django 3.1.3 on 2020-11-30 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booth_equipment', models.CharField(max_length=100)),
                ('Booth_cost', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'Booth',
            },
        ),
        migrations.CreateModel(
            name='Booth_Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BReserve_student', models.IntegerField()),
                ('BReserve_booth', models.IntegerField()),
                ('BReserve_timeslot', models.TimeField()),
                ('CReserve_date', models.TimeField()),
            ],
            options={
                'db_table': 'Booth_Reserve',
            },
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timeslot_start_time', models.TimeField()),
                ('Timeslot_end_time', models.TimeField()),
            ],
            options={
                'db_table': 'Timeslot',
            },
        ),
    ]
