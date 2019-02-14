from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def home_view(request):

    my_context = {
        'title': "This is about us",
        'my_number': 123,
        'my_list': [5, 4, 3, 2, 1],
        'my_html': "<h3>Hey there planet</h3>"
    }
    return render(request, "products/home.html", my_context)


def posh_view(request):

    return render(request, "products/posh.html", {})


def contact_view(request):

    return render(request, "products/contact.html", {})


def about_view(request):
    my_context = {
        'my_text': "This is about us",
        'my_number': 123,
        'my_list': ['a', 'b', 'c', 'd', 'e'],
    }
    return render(request, "products/about.html", my_context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj,
        'title': obj.title,
        'description': obj.description,
    }
    return render(request, "products/detail.html", context)