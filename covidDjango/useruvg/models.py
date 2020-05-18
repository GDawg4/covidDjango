from django.db import models

# Create your models here.
class Useruvg(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=50)
    enabled = models.BooleanField()
    firstname = models.CharField(max_length=50)
    lastpasswordresetdate = models.DateTimeField()
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    username = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'useruvg'