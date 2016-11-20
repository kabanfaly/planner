from django.shortcuts import render, get_object_or_404
from employee.models import Employee


def index(request):

    """ Display all Employee"""
    employees = Employee.objects.all()
    return render(request, 'employee/index.html', {'employees': employees})


def display(request, id):

    """ Display an employee identified by the given 'id' """
    employee = get_object_or_404(Employee, id=id)

    return render(request, 'employee/info.html', {'employee': employee})
