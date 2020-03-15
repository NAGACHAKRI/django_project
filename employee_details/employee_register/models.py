from django.db import models

class Position(models.Model):
    title=models.CharField(max_length=20)
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
 


