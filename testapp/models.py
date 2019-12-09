from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    eaddr = models.CharField(max_length=100)
    esal = models.FloatField()

"""def __str__(self):
        return self.eno,self.ename,self.eaddr,self.esal"""
