from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    my_context = {
        'my_text': "This is about us",
        'my_number': 123,
        'my_list': [5, 4, 3, 2, 1],
    }
    return render(request, "products/about.html", my_context)


def posh_view(request):
    return render(request, "products/about.html", {})

def contact_view(request):
    return render(request, "products/contact.html", {})

def about_view(request):
    my_context = {
        'my_text': "This is about us",
        'my_number': 123,
        'my_list': [5, 4, 3, 2, 1],
    }
    return render(request, "products/about.html", my_context)
