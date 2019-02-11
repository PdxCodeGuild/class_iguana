from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('gtn/', include('guess_the_number.urls')),
    path('admin/', admin.site.urls),
]
