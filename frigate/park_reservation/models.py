from django.db import models
from django.conf import settings


ROLES = {
    'manage': 'Manger',
    'employee': 'Employee'
}



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    # role = models.CharField(choices=ROLES)

    def __str__(self):
        return f'Profile for user {self.user.username}'
