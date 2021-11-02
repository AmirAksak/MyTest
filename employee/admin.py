from django.contrib import admin

from employee.models import Employee, Departments, Posts


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'second_name', 'age')
    list_display_links = ('last_name',)
    search_fields = ('last_name',)


class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'boss_id')
    list_display_links = ('name',)
    search_fields = ('name',)

class PostsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Posts, PostsAdmin)