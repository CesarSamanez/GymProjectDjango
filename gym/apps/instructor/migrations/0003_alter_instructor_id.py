# Generated by Django 4.1.3 on 2022-11-23 01:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0002_alter_instructor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9b4dd8cf-92be-479a-98d6-0cc46d757590'), editable=False, primary_key=True, serialize=False),
        ),
    ]