from django.db import models

class Condition(models.Model):
 name =  models.CharField(max_length=60)
 state = models.CharField(max_length=10)

 def __str__(self):
     return self.name
