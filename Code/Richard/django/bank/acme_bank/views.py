from django.shortcuts import render
from django.http import HttpResponse
from .models import Account

def account_detail(request, account_id):
    account = Account.objects.get(id=account_id)
    print(account.balance)
    return render(request, 'acme_bank/account_detail.html', {'account': account})
