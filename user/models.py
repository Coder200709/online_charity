from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=16, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
