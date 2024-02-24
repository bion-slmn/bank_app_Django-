from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Account(BaseModel):
    name = models.CharField(max_length=50, null=False)
    balance = models.FloatField(default=True)

    def __str__(self):
        return self.name


class TransactionHistory(BaseModel):
    withdraw = models.FloatField(default=0.0)
    deposit = models.FloatField(default=0.0)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transaction for {self.account.name}"
