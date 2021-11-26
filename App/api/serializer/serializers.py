from rest_framework import serializers

from api.models.models import Order, Product

class OrderSerializer(serializers.ModelSerializer):
   class Meta:
       model = Order
       fields = ('id','payment_status','order_status','price','unit_cost','quantity','name')


class ProductSerializer(serializers.ModelSerializer):
   class Meta:
       model = Product
       fields = ('id','name', 'unit_cost', 'price','unit_available')