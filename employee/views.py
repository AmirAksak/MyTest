from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.response import Response
from .service import EmployeeFilter
from rest_framework.views import APIView
from employee.models import Employee, Departments
from employee.serializers import EmployeesListSerializer, EmployeeDetailSerializer, DepartmentsListSerializer, \
    EmployeeAddSerializer, EmployeeDeletteSerializer, DepartmentsEmployeesListSerializer


# Create your views here.


class EmployeesListView(generics.ListAPIView):
    '''Список сотрудников'''
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeesListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EmployeeFilter
    def get_queryset(self):
        employees = Employee.objects.all()
        return employees


class EmployeeDetailView(APIView):
    '''Полные данные по работнику'''
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeDetailSerializer(employee)
        return Response(serializer.data)


class DepartmentsListView(APIView):
    '''Список департаментов'''
    def get(self, request):
        qset='''select distinct
	ed.id
	,ed.name
	,ed.boss_id
	,sum(ee.salary) over (partition by ed.id) sum_salary
	,count(ee.id) over (partition by ed.id) count_employees
from employee_departments ed
	join employee_employee_department_id eedi on eedi.departments_id = ed.id
	join employee_employee ee on ee.id = eedi.employee_id
	order by ed.id
;'''
        # Количество работников + сумма всех зарплат в отделе
        # Такое лучше сделаю через запрос
        departments = Departments.objects.raw(qset)
        serializer = DepartmentsListSerializer(departments, many=True)
        return Response(serializer.data)


class DepartmentsEmployeesListView(APIView):
    '''Список департаментов с сотрудниками'''
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        departments = Departments.objects.all().order_by('name')
        serializer = DepartmentsEmployeesListSerializer(departments, many=True)
        return Response(serializer.data)


class EmployeeAddView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeAddSerializer


class EmployeeDeletteView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeDeletteSerializer
    def get_queryset(self):
        employees = Employee.objects.all()
        return employees
