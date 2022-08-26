from django.db import models


# Create your models here.


class Employee(models.Model):
    Name=models.CharField(max_length=25)
    Address=models.TextField(max_length=50)
    Mobile_no=models.CharField(max_length=10)
    Emp_role=models.CharField(max_length=15)

    def __str__(self):
        return self.Name
