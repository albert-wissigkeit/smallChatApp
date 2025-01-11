from django.db import models

# Create your models here.
class Chat(models.Model): 
    name = models.CharField(max_length=255, blank=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
