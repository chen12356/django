from django.db import models

# Create your models here.



class BathCenter(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()

    class Meta:
        db_table = 'bathcenter'