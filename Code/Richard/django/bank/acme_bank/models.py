from django.db import models

# Create your models here.

class AccountType(models.Model):
    acct_type = models.PositiveSmallIntegerField()

    def __repr__(self):
        return self.acct_type
    
class AccountHolder(models.Model):
    corporate_name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200)
    personal_name = models.CharField(max_length=200, null=True, blank=True)
    
    class Meta:
        ordering = ['surname', 'personal_name']

    def __str__(self):
        return f'{self.surname}, {self.personal_name}'

class Account(models.Model):
    balance = models.DecimalField(max_digits=999, decimal_places=2)
    account_holder = models.ManyToManyField('AccountHolder')
    acct_type = models.ForeignKey('AccountType', on_delete='PROTECT')
    interest_rate = models.DecimalField(max_digits=3, decimal_places=3)


