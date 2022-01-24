from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.name} -- {self.email}"