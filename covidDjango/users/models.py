from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    consent = models.BooleanField()
    nametag = models.CharField(unique=True, max_length=100)
    useruvg = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return '{}'.format(self.nametag)