from django.db import models

# Create your models here.

class AccountType(models.Model):
    acct_type = models.PositiveSmallIntegerField()

    def __str__(self):
        if self.acct_type == 1:
            return "Checking"
        elif self.acct_type == 2:
            return "Savings"
        elif self.acct_type ==3:
            return "Credit"

class AccountHolder(models.Model):
    name = models.CharField(max_length=200)
    personal_name = models.CharField(max_length=200, null=True, blank=True)
    is_corporation = models.BooleanField()
    
    class Meta:
         ordering = ['name', 'personal_name']

    def __str__(self):
        if self.is_corporation:
            return self.name
        else:
            return f'{self.name}, {self.personal_name}'

class Account(models.Model):
    balance = models.DecimalField(max_digits=999, decimal_places=2)
    account_holder = models.ManyToManyField('AccountHolder')
    acct_type = models.ForeignKey('AccountType', on_delete='PROTECT')
    interest_rate = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.account_holder.name

    # def display_account_holder(self):
    #     return ', '.join(self.account_holder.name, self.account_holder.personal_name)

