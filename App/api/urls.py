from django.urls import include, path

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import ProductViewAllSet, StockView, OrderView, OrderSummaryView


urlpatterns = [
    path('Products/', ProductViewAllSet.as_view()),
    path('Products/ByName', StockView.as_view()),
    path('Products/Order', OrderView.as_view()),
    path('Products/Order/Summary', OrderSummaryView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)