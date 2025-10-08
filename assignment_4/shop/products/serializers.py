from rest_framework import serializers
from .models import Product, Order, OrderItem


# ---------- PRODUCT SERIALIZER ----------
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


# ---------- ORDER ITEM SERIALIZER ----------
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.name")
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ["id", "product", "product_name", "quantity", "price", "subtotal"]

    def get_subtotal(self, obj):
        return obj.subtotal()


# ---------- ORDER SERIALIZER ----------
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ["id", "user", "total_price", "status", "created_at", "items"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            product = item_data["product"]
            quantity = item_data["quantity"]
            price = product.price
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)

            # reduce product stock
            product.stock -= quantity
            product.save()
        order.calculate_total()
        return order
