from django.contrib import admin

# Register your models here.
from .models import AccountType, AccountHolder, Account

admin.site.register(Account)
admin.site.register(AccountHolder)
admin.site.register(AccountType)

# @admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('display_account_holder', 'acct_type', 'balance')