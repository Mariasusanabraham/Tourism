
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from apps_tourism import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps_tourism.urls')),

]
