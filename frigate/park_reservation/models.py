from django.contrib.auth.models import User
from django.db import models

choice = [('Manager', 'Manager'), ('Employee', 'Employee')]


class Profile_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=choice, default='Employee')

    def __str__(self):
        return self.user.username
