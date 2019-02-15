from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect(reverse('products:home'))
    else:
        form = UserCreationForm()
    return render(request, 'users/registration.html', {'form': form})

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error