from django.contrib import admin
from django.urls import path, include
from to_do_list_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('to_do_list_app.urls')),
]
