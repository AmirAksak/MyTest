from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .models import Employee

class PaginatorEmployees(PageNumberPagination):
    page_size = 2
    max_page_size = 5000


class EmployeeFilter(filters.FilterSet):
    last_name = filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    department_id = filters.Filter('department_id')

    class Meta:
        model = Employee
        fields = ['department_id', 'last_name']
