from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('work/<int:work_id>/delete/', views.delete_work, name='delete_work'),
    path('work/<int:work_id>/done/', views.mark_work_as_done, name='mark_work_as_done'),
]
