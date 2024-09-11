from django.db import models

# Create your models here.

class Work(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
