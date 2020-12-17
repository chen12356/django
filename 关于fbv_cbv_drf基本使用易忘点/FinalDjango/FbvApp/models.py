from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    class Meta:
        db_table = 'animal'

    def to_dict(self):
        return {'name':self.name,'age':self.age}
