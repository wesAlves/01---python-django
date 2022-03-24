from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField('date published')
    deadline_date = models.DateField(null=True)
    is_done = models.BooleanField(default=False)