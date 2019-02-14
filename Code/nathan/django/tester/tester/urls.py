"""tester URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from ..users.views import register_view
import os
os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from users.views import register_view


urlpatterns = [
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', views.LoginView.as_view(template_name='products/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='products/logout.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)