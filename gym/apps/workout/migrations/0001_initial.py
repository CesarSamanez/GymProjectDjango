# Generated by Django 4.1.3 on 2022-11-22 23:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instructor', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('a4a6e586-76b8-4b13-bc61-009a28d02bf8'), editable=False, primary_key=True, serialize=False)),
                ('workout_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('374e447b-9638-4e6b-91de-d6f30df3fcc3'), editable=False, primary_key=True, serialize=False)),
                ('work_out_date_time', models.DateTimeField(default=datetime.datetime(2022, 11, 22, 18, 7, 25, 369012))),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.instructor')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.workout')),
            ],
        ),
    ]
