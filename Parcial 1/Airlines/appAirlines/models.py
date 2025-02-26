from django.db import models

# Create your models here.

#flight model: id auto increment primary key, name, type: national or international, price
class Airline(models.Model):
    FLIGTH_TYPE = (
        ('N', 'National'),
        ('I', 'International')
    )
    flyId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='nombre de vuelo')
    type = models.CharField(max_length=1,verbose_name='tipo de vuelo', choices=FLIGTH_TYPE)
    price = models.IntegerField(verbose_name='Precio')

    def __str__(self):
        return self.name