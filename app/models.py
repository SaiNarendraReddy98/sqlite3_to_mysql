from django.db import models

# Create your models here.

class School(models.Model):
    Sname = models.CharField(max_length=100,primary_key=True)
    Slocation = models.CharField(max_length=100)
    def __str__(self):
        return self.Sname


class Student(models.Model):
    Stname = models.CharField(max_length=100)
    Sname = models.ForeignKey(School,on_delete=models.CASCADE)
    def __str__(self):
        return self.Stname
    
    