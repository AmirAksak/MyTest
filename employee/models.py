from django.db import models

# Create your models here.


class Departments(models.Model):    # Отделы
    name = models.CharField(max_length=300, verbose_name='Название департамент')
    boss_id = models.IntegerField(verbose_name='Директор департамента')


    def __str__(self):
        return self.name

    class Meta:         # Отображение в админке
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class Posts(models.Model):          # Должности
    name = models.CharField(max_length=300, verbose_name='Название должности')

    def __str__(self):
        return self.name

    class Meta:         # Отображение в админке
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Employee(models.Model):       # Сотрудники
    last_name = models.CharField(max_length=20, verbose_name='Фамилия сотрудника')
    first_name = models.CharField(max_length=20, verbose_name='Имя сотрудника')
    second_name = models.CharField(max_length=20, verbose_name='Отчество сотрудника', blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    post_id = models.ManyToManyField(Posts, verbose_name='Должность')
    salary = models.IntegerField(verbose_name='Оклад')
    age = models.IntegerField(verbose_name='Возраст')   # Обычно вычисляется в запросе от birthday. Оставим age по заданию
    department_id = models.ManyToManyField(Departments, verbose_name='Департамент', related_name='employees')


    def __str__(self):
        return self.last_name

    class Meta:         # Отображение в админке
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


