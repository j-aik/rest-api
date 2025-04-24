from django.urls import path
from.import views

urlpatterns = [
    path('',views.index1,name="index1"),
    path('items/<int:id>/',views.index,name="index"),
    path('student_list_view',views.student_list_view,name="student_list_view"),
    path('todos/', views.todo_list_create, name='todo_list_create'),
    path('todos/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('number_list_view/', views.number_list_view, name='number_list_view'),
    path('user_register/',views.user_register,name="user_register"),
    path('token/', views.custom_token_obtain_pair, name='custom_token_obtain_pair'),
    path('saved_picture_view/', views.saved_picture_view, name='saved_picture_view')
]