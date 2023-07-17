from django.db import models
from django.utils import timezone

# Create your models here.

class List(models.Model):
    item = models.CharField(max_length=150)
    description = models.CharField(max_length = 259,null=True)
    completed = models.BooleanField(default=False)
    start_date= models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.item + ' | ' + str(self.completed)