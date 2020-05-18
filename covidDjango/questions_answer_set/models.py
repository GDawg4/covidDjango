from django.db import models

# Create your models here.
class QuestionsAnswerSet(models.Model):
    question_set = models.OneToOneField('questions.Questions', models.DO_NOTHING, primary_key=True)
    answer_set = models.ForeignKey('answers.Answers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questions_answer_set'
        unique_together = (('question_set', 'answer_set'),)