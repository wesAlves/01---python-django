from django.urls import path

from . import views

app_name = 'todoBackend'

urlpatterns = [
    path('', views.index, name='index'),
    # path('<TodoList_id>/', views.detail, name='detail'),
    path('<TodoList_id>/', views.edit, name='edit'),
    path('<TodoList_id>/delete', views.delete, name='delete')
]
