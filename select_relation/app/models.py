from django.db import models

# Create your models here.

class HeadOfDept(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Department(models.Model):
    name=models.CharField(max_length=10)
    hod=models.ForeignKey(HeadOfDept,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.name

class House(models.Model):
    name=models.CharField(max_length=10)
    head=models.CharField(max_length=10,default=' ')
    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=20)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    house=models.ForeignKey(House,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.name

class Contest(models.Model):
    name=models.CharField(max_length=20)
    prize=models.CharField(max_length=10,default=' ')
    stud = models.ManyToManyField(Student)
    def __str__(self):
        return self.name