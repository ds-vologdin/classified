from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ads/', include('advertisement.urls')),
    path('admin/', admin.site.urls),
]
