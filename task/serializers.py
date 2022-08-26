from rest_framework.serializers import ModelSerializer
from .models import (
                    Product
)


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["Name", "item_cost", "stock_quantity", "volume"]