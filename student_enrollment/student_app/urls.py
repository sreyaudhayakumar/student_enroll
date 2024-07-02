from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('base2/', views.base2, name='base2'),
    path('student/create/', views.create_student, name='create_student'),
    path('student/view/', views.view_students, name='view_students'),
    path('student/update/<int:id>/', views.update_student, name='update_student'),
    path('student/delete/<int:id>/', views.delete_student, name='delete_student'),
]
