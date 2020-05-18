from django.db import models

# Create your models here.
class Authority(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'authority'