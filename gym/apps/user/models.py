from django.db import models
import uuid


class User(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False
    )
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
