from django.db import models
from django.contrib.auth.models import AbstractUser
from frigate.settings import ROLES


CHOICES = (
    ('Manager', 'Manager'),
    ('Employee', 'Employee', )
)


class MyUser(AbstractUser):
    role = models.CharField(max_length=8, choices=CHOICES)

    @property
    def is_moderator(self):
        return self.role == ROLES['MODERATOR_ROLE']


class Parking_place(models.Model):
    owner = models.CharField(max_length=30)
    from_time = models.TimeField(editable=True, default='10:00')
    to_time = models.TimeField(editable=True, default='17:00')
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.owner
