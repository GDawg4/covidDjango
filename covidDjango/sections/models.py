from django.db import models

# Create your models here.
class Sections(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    id_questionnaire_type = models.ForeignKey('questionnaire_type.QuestionnaireType', models.DO_NOTHING, db_column='id_questionnaire_type')

    class Meta:
        managed = False
        db_table = 'sections'

    def __str__(self):
        return '{}'.format(self.description)