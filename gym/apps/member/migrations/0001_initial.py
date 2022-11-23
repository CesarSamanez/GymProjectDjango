# Generated by Django 4.1.3 on 2022-11-22 23:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('75e3a7fc-1c1e-4ec0-a73c-51146a249915'), editable=False, primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=15)),
                ('membership_period', models.CharField(max_length=15)),
                ('membership_amount', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('069b92a5-bb58-492f-80b4-f59e9937a699'), editable=False, primary_key=True, serialize=False)),
                ('member_id_nro', models.CharField(max_length=15)),
                ('member_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('age', models.IntegerField(max_length=3)),
                ('gender', models.IntegerField(max_length=1)),
                ('joining_date', models.DateField()),
                ('end_of_membership_date', models.DateField()),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.membershiptype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]