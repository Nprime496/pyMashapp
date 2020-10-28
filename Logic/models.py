from django.db import models


# Create your models here.

class Personne(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    nom=models.CharField(max_length=50)
    description=models.CharField(max_length=250)


class Filleul(Personne):
    parrain=models.ForeignKey(Personne,on_delete=models.CASCADE,related_name='mon_parrain')


