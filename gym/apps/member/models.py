from django.db import models
import uuid

from ..user.models import User


class MembershipType(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=15)
    membership_period = models.CharField(max_length=15)
    membership_amount = models.FloatField()


class Member(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    member_id_nro = models.CharField(max_length=15)
    member_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    age = models.IntegerField(max_length=3)
    gender = models.IntegerField(max_length=1)  # [0] female, [1] male
    joining_date = models.DateField()
    end_of_membership_date = models.DateField()
