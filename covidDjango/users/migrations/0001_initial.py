# Generated by Django 3.0.4 on 2020-05-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('consent', models.BooleanField()),
                ('nametag', models.CharField(max_length=100, unique=True)),
                ('useruvg', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
