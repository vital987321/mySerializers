from rest_framework import serializers
from myapp.models import User, Product, Purchase


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    # client = UserSerializer()
    # product = ProductSerializer()
    # client = serializers.PrimaryKeyRelatedField(read_only=True)
    # product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model= Purchase
        fields = ['client', 'product', 'product_amount']
