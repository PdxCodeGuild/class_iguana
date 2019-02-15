from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html', {})

def account_detail(request, account_id):
    account = Account.objects.get(id=account_id)
    print(account.balance)
    return render(request, 'acme_bank/account_detail.html', {'account': account})

def transaction_window(request, account_id):
    account = Account.objects.get(id=account_id)

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    next = request.POST['next']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if next == '':
            return HttpResponseRedirect(reverse('users:protected'))
        return HttpResponseRedirect(next)
    return HttpResponseRedirect(reverse('users:index'))