from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError
from .models import Account, TransactionHistory


@receiver(pre_save, sender=TransactionHistory)
def before_withdraw(sender, instance, **kwargs):
    '''signal to check if the balance is more than the withdraw aount
    if not raise an exception
    '''
    if instance.withdraw > 0 and instance.account.balance < instance.withdraw:

        raise ValidationError("Insufficent fund ")



@receiver(post_save, sender=TransactionHistory)
def after_deposit(sender, instance, created, **kwargs):
    '''
    this signal updates the account balance of the user after withdraw or balance
    '''
    if created:
    
        if instance.withdraw > 0:
            instance.account.balance -= instance.withdraw

        if instance.deposit > 0:
            instance.account.balance += instance.deposit

        instance.account.save()

