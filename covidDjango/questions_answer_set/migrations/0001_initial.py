# Generated by Django 3.0.4 on 2020-05-17 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsAnswerSet',
            fields=[
                ('question_set', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='questions.Questions')),
            ],
            options={
                'db_table': 'questions_answer_set',
                'managed': False,
            },
        ),
    ]
