from django.db import models

# Create your models here.
class Chat(models.Model): 
    name = models.CharField(max_length=255, blank=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)   # muss noch auf readonly im serializer gesetzt werden oder im admin interface, damit es nicht über das frontend geändert werden kann
