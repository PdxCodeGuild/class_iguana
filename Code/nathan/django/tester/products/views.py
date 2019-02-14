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


def contact_view(request):

    return render(request, "products/contact.html", {})


def about_view(request):
    my_context = {
        'my_text': "This is about us",
        'my_number': 123,
        'my_list': ['a', 'b', 'c', 'd', 'e'],
    }
    return render(request, "products/about.html", my_context)



def products_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "products/detail.html", context)


def cart_view(request):

    return render(request, "products/cart.html", {})
