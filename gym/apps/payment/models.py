from datetime import datetime

from django.db import models
import uuid

from ..member.models import Member


class Payment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False
    )
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_datetime = models.TimeField(default=datetime.now())
