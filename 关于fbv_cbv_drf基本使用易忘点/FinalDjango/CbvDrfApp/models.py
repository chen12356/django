from django.db import models

# Create your models here.


class Women(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=18)

    class Meta:
        db_table = 'women'