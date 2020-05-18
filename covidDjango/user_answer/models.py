from django.db import models

# Create your models here.
class UserAnswer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    report_date = models.DateTimeField(blank=True, null=True)
    id_answer = models.ForeignKey('answers.Answers', models.DO_NOTHING, db_column='id_answer')
    id_questionnaire_type = models.ForeignKey('questionnaire_type.QuestionnaireType', models.DO_NOTHING, db_column='id_questionnaire_type')
    id_questions = models.ForeignKey('questions.Questions', models.DO_NOTHING, db_column='id_questions')
    id_user = models.ForeignKey('users.Users', models.DO_NOTHING, related_name='answers_given', db_column='id_user')

    class Meta:
        managed = False
        db_table = 'user_answer'

    def __str__(self):
        return 'Answer given by {} with {}'.format(self.id_user, self.id_answer)