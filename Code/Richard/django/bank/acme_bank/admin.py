from django.contrib import admin

from acme_bank.models import AccountType, AccountHolder, Account

admin.site.register(AccountType)
admin.site.register(AccountHolder)
admin.site.register(Account)
