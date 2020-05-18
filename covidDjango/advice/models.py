from django.db import models

# Create your models here.
class Advice(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=10000, blank=True, null=True)
    image = models.CharField(max_length=10000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advice'