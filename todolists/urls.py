from django.urls import path
from todolists import views

urlpatterns = [
    path('', views.ToDoListView.as_view(), name='todolist_view'),
    path('<int:todolist_id>/', views.ToDoListDetailView.as_view(), name='todolist_detail'),

]