# Generated by Django 4.1.3 on 2022-11-23 00:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bdb509ca-7702-4a68-96af-d505b75ca945'), editable=False, primary_key=True, serialize=False),
        ),
    ]