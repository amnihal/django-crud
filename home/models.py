from django.db import models

# Create your models here.

class Marklist(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    grade=models.CharField(max_length=30) 

    def __str__(self):
        return self.name
    

