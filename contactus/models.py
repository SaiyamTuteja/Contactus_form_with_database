from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    status = models.BooleanField(null=True)

    def __str__(self):
        return f'{self.name} + {self.message}'
