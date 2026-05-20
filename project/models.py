from django.db import models

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)