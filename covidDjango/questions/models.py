from django.db import models

# Create your models here.
class Questions(models.Model):
    id = models.BigAutoField(primary_key=True)
    correlative = models.IntegerField()
    display = models.BooleanField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    required = models.BooleanField(blank=True, null=True)
    selected = models.BooleanField(blank=True, null=True)
    title = models.CharField(max_length=5000, blank=True, null=True)
    id_question_type = models.ForeignKey('question_type.QuestionType', models.DO_NOTHING, db_column='id_question_type')
    id_questionnaire = models.ForeignKey('questionnaire_type.QuestionnaireType', models.DO_NOTHING, db_column='id_questionnaire')
    id_sections = models.ForeignKey('sections.Sections', models.DO_NOTHING, db_column='id_sections')

    class Meta:
        managed = False
        db_table = 'questions'

    def __str__(self):
        return self.name