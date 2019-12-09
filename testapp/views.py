from django.shortcuts import render
from .models import Employee
# Create your views here.
def emplyoee_info_view(request):
    employees = Employee.objects.all()
    return render(request,'testapp/results.html',{'employees':employees})