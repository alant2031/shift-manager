from django.db import models
from django.contrib.auth import get_user_model


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Account(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True, unique=True)
    role = models.CharField(
        max_length=100,
        choices=[("admin", "Admin"), ("member", "Member")],
        default="member",
    )
    is_active = models.BooleanField(default=False)


class Commitment(BaseModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
    position = models.ForeignKey("Position", on_delete=models.SET_NULL)


class Position(BaseModel):
    title = models.CharField(max_length=100)


class OpenDate(BaseModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date1 = models.DateField()
    date2 = models.DateField(null=True, blank=True)
    date3 = models.DateField(null=True, blank=True)
