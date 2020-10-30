from django.db import models

# Create your models here.
class LoginInfo(models.Model):
    username = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    

    def __str__(self):
        return self.username