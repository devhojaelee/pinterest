from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False) #char이 null이 되도 괜찮은지. 안괜찮으니 false.
