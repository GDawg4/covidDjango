from django.db import models

# Create your models here.
class Answers(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    id_father = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'

    def __str__(self):
        return self.description