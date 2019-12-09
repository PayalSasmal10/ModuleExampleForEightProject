import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','eightproject_models.settings')
django.setup()

from .testapp.models import Employee
from faker import Faker
from random import *

fake = Faker()
def populate(n):
    for i in range(n):
        feno = randint(1001,9999)
        fname = fake.name()
        faddr = fake.city()
        fsal  = randint(10000,99999)
        emp_record = Employee.objects.get_or_create(eno = feno,ename = fname,eaddr = faddr,esal = fsal)


populate(30)
