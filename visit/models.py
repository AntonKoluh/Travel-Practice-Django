from django.db import models
from project.models import Projects
# Create your models here.

class Visit(models.Model):
    place_id = models.IntegerField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    is_visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)