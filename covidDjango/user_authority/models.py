from django.db import models

# Create your models here.
class UserAuthority(models.Model):
    user = models.ForeignKey('useruvg.Useruvg', models.DO_NOTHING)
    authority = models.ForeignKey('authority.Authority', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_authority'