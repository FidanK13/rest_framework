from django.db import models
from django.contrib.auth  import get_user_model
User = get_user_model()

# Create your models here.

class PasswordModel(models.Model):
    confirm_password = models.CharField(max_length=24,null=True, blank=True)

class UserModel(models.Model):
    username = models.CharField(max_length=24, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=24,null=True, blank=True)
    confirm_password = models.CharField(max_length=24,null=True, blank=True)
    def __str__(self):
        return f'{self.username}'

class BookModel(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name}'


