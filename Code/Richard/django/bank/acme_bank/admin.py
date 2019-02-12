from django.contrib import admin

# Register your models here.
from .models import AccountType, AccountHolder, Account

admin.site.register(Account)
admin.site.register(AccountHolder)
admin.site.register(AccountType)