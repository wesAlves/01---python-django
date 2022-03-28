from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'todoBackend/', include('todoBackend.urls')),
    path(r'api/', include('todoListRestAPI.urls')),
    path('admin/', admin.site.urls),
]





# app_name = 'todoListRestAPI'
