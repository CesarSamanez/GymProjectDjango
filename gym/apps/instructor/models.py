from django.db import models
import uuid

from ..user.models import User


class Instructor(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instructor_name = models.CharField(max_length=40)
    email = models.CharField(max_length=30)
