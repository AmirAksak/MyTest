from django.urls import path
from employee import views

urlpatterns = [
    path('employees/', views.EmployeesListView.as_view()),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view()),
    path('addemployee/', views.EmployeeAddView.as_view()),
    path('delemployee/<int:pk>', views.EmployeeDeletteView.as_view()),
    path('departments/', views.DepartmentsListView.as_view()),
    path('departmentsempl/', views.DepartmentsEmployeesListView.as_view()),

]