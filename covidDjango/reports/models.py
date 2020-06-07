from django.db import models

# Create your models here.
class Report(models.Model):
    user = models.ForeignKey(
        'users.Users',
        on_delete=models.CASCADE
    )
    date = models.DateField(auto_now=False)
    isConfirmed = models.BooleanField(default=False, null=False)
    isSuspected = models.BooleanField(default=False, null=False)
    isContacted = models.BooleanField(default=False, null=False)
    isDismissed = models.BooleanField(default=False, null=False)