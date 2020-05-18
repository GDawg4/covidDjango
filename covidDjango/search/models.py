from django.db import models

# Create your models here.
class Search(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_tag = models.CharField(unique=True, max_length=100)
    useruvg = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'search'
