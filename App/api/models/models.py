from django.db import models

# Create your models here.

class Product(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)
   unit_cost = models.FloatField()
   price = models.FloatField()
   unit_available = models.IntegerField()

   class Meta:
      db_table = 'PRODUCT'


class Order(models.Model):
   id = models.AutoField(primary_key=True)
   payment_status = models.CharField(max_length=100)
   order_status = models.CharField(max_length=100)
   price = models.FloatField()
   unit_cost = models.FloatField()
   quantity = models.IntegerField()
   name = models.CharField(max_length=100)

   class Meta:
      db_table = 'Orders'