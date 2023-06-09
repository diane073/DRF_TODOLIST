from django.db import models
from django.conf import settings
# Create your models here.


class ToDoList(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    completion_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content