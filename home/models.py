from django.db import models

# Create your models here.
class info(models.Model):
    squad = models.CharField(max_length=122)
    teams = models.TextField()