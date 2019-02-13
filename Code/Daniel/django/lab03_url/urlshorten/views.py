from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Url
import random
import string

def index(request):
    if 'id' in request.GET:
        url_pair = Url.objects.get(id=request.GET['id'])
        context = {'short_url': url_pair}
    else:
        context = {}
    return render(request, 'urlshorten/index.html', context)

def saveurl(request):
    url = request.POST['long_url']

    code = ''
    for i in range(7):
        code += random.choice(string.ascii_letters)
    
    url_pair = Url(code=code, url=url)
    url_pair.save()

    return HttpResponseRedirect(reverse('urlshorten:index')+'?id=' + str(url_pair.id))

def redirect_url(request, code):
    pair = Url.objects.get(code=code)
    if ('http' in pair.url):
        url = pair.url
    else:
        url = 'https://'+ str(pair.url)
    return redirect(url)