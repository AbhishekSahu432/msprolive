from django.db import models
class Stu(models.Model):
    name=models.CharField(max_length=25)
    roll=models.IntegerField()
    email=models.EmailField(max_length=30)
    address=models.TextField()
    mob=models.IntegerField()
    def __str__(self) -> str:
        return self.name
