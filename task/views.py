# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            name = data.get("Name", None)
            item_cost = data.get("item_cost", None)
            stock_quantity = data.get("stock_quantity", None)
            print(item_cost)
            print(stock_quantity)
            volume = int(item_cost)*int(stock_quantity)
            product = Product.objects.create(
                Name=name,
                item_cost=item_cost,
                stock_quantity=stock_quantity,
                volume=volume,
                )
            serializer = self.get_serializer(product).data
            return Response(
                data={
                    "message": " Successfully completed",
                    "details": serializer,
                    "success": True,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as exp:
            return Response("Invalid")