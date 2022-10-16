from Employees import views
from django.urls import path

urlpatterns=[
    path('department/<int:id>/', views.departmentApi),
    path('department/', views.departmentApi),

    path('employee/<int:id>/', views.employeeApi),
    path('employee/', views.employeeApi),
]