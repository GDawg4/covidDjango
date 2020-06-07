from django.db import models


# Create your models here.
class QuestionnaireType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questionnaire_type'
