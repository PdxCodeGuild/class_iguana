from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def home_view(request):

    my_context = {
        'title': "has good deals",
        'my_number': 123,
        'my_list': ['Plush Toys', 'Posters', 'Clothes', 'MP3\'s', 'Foreign Candy'],
        'my_html': "<h3>sells lots of things</h3>"
    }
    return render(request, "products/home.html", my_context)


def contact_view(request):

    return render(request, "products/contact.html", {})


def products_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "products/detail.html", context)

#
# def cart_view(request):
#
#     return render(request, "products/cart.html", {})
# <nav>
#     <a href="{% url 'users:login' %}">Login</a>
#     <a href="{% url 'users:logout' %}">Logout</a>
#     <a href="{% url 'users:register' %}">Register</a>
# </nav>