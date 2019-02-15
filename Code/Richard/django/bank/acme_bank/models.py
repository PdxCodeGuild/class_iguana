from django.db import models
import uuid # Required for unique book instances


# Create your models here.

class AccountType(models.Model):
    account_type = models.PositiveSmallIntegerField()

    def __str__(self):
        if self.account_type == 1:
            return 'Checking'
        elif self.account_type == 2:
            return 'Savings'
        elif self.account_type == 3:
            return 'Credit'
    
class AccountHolder(models.Model):
    name = models.CharField(max_length=200)
    personal_name = models.CharField(max_length=200, null=True, blank=True)
    is_corporate = models.BooleanField()

    class Meta:
        ordering = ['name', 'personal_name']

    def __str__(self):
        if self.is_corporate:
            return self.name
        else:
            return f'{self.name}, {self.personal_name}'

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Account number')
    account_type = models.ForeignKey('AccountType', on_delete=models.CASCADE)
    account_holders = models.ManyToManyField('AccountHolder')
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=6, decimal_places=3)


    def __str__(self):
        return f'{"; ".join([str(account_holder) for account_holder in self.account_holders.all()])} - {self.account_type}'

class Transactions(models.Model):
    date = models.DateField()
    transaction_type = models.PositiveSmallIntegerField()

    """
    note: 
    1 : deposit
    2 : withdrawal
    3 : assess_interest
    """