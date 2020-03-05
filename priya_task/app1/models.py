from django.db import models

# Create your models here.
class Data_Saved(models.Model):
    sym=models.CharField(max_length=30,default=False)
    series=models.CharField(max_length=30)
    open=models.DecimalField(max_digits=10,decimal_places=2)
    high=models.DecimalField(max_digits=10,decimal_places=2)
    low=models.DecimalField(max_digits=10,decimal_places=2)
    close=models.DecimalField(max_digits=10,decimal_places=2)
    last=models.DecimalField(max_digits=10,decimal_places=2)
    pre=models.DecimalField(max_digits=10,decimal_places=2)
    totqty=models.IntegerField()
    data=models.CharField(max_length=50,default=False)

