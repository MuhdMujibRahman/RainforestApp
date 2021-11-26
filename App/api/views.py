from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializer.serializers import ProductSerializer, OrderSerializer
from api.models.models import Product, Order

from api.services.update_order import UpdateOrder
from api.services.order_summary import OrderSummary

class ProductViewAllSet(APIView):
   def get(self, request, format=None):
      products = Product.objects.all()
      serializer = ProductSerializer(products, many=True)
      return Response(serializer.data)

   def post(self, request, format=None):
      serializer = ProductSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StockView(APIView):

   def get_object(self, request):
      try:
         return Product.objects.get(name__exact=request.data.get('name'))
      except Product.DoesNotExist:
         raise Http404

   def get(self, request, format=None):
      products = self.get_object(request)
      serializer = ProductSerializer(products)
      return Response(serializer.data)

   def put(self, request, format=None):
      products = self.get_object(request)
      serializer = ProductSerializer(products, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderView(APIView):


   def get(self, request, format=None):
      orders = Order.objects.all()
      serializer = OrderSerializer(orders, many=True)
      return Response(serializer.data)

   # def put(self, request, format=None):
   #    orders = self.get_object(request)
   #    serializer = OrderSerializer(orders, data=request.data)
   #    if serializer.is_valid():
   #       serializer.save()
   #       return Response(serializer.data)
   #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def post(self, request, format=None):
      serializer = OrderSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         update_stock = UpdateOrder(request)
         response = update_stock.update_table()
         return Response(response, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderSummaryView(APIView):

   def get(self, request, format=None):
      orders = OrderSummary(request)
      api = orders.get_created_orders()
      response = orders.get_summarized_data(api)
      serializer = OrderSerializer(orders, many=True)
      return Response(response)
