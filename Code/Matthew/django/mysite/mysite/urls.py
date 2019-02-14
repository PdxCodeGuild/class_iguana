from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('gtn/', include('guess_the_number.urls')),
    path('students/', include('students.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
