from django.db import models


class UserModel(models.Model):
    class Meta:
        db_table = "User"

    email = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)