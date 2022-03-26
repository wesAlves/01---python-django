from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'todoList', views.TodoListViewSet)


app_name = 'todoListRestAPI'

urlpatterns = [
    path('', include(router.urls) )
]
