from rest_framework import serializers
from employee.models import Employee, Departments


class EmployeesListSerializer(serializers.ModelSerializer):
    '''Список всех сотрудников'''
    class Meta:
        model = Employee
        fields = ('id', 'last_name', 'first_name', 'second_name', 'age')


class EmployeeDetailSerializer(serializers.ModelSerializer):
    '''Полные данные по работнику'''
    post_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    department_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeAddSerializer(serializers.ModelSerializer):
    '''Добавление сотрудника'''
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeDeletteSerializer(serializers.ModelSerializer):
    '''Удаление сотрудника'''
    class Meta:
        model = Employee
        fields = ('id', 'last_name')


class DepartmentsListSerializer(serializers.ModelSerializer):
    '''Список департаментов'''
    #employees = EmployeeAddSerializer(many=True)
    count_employees = serializers.IntegerField()
    sum_salary = serializers.IntegerField()
    class Meta:
        model = Departments
        fields = ('id', 'name', 'boss_id', 'count_employees', 'sum_salary')


class DepartmentsEmployeesListSerializer(serializers.ModelSerializer):
    '''Список департаментов с сотрудниками'''
    employees = EmployeeAddSerializer(many=True)
    class Meta:
        model = Departments
        #fields = '__all__'
        fields = ('id', 'name', 'employees', 'boss_id')