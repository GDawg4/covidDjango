# Generated by Django 3.0.4 on 2020-05-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sections',
                'managed': False,
            },
        ),
    ]