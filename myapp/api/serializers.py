from rest_framework import serializers
from myapp.models import User, Product, Purchase


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','wallet',]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model= Purchase
        fields = ['client', 'product', 'product_amount']


class PurchaseWithUserSerializer(serializers.ModelSerializer):
    client=UserSerializer(many=False)
    class Meta:
        model = Purchase
        fields = ['client', 'product', 'product_amount']


class UserWithPurchasesSerializer(serializers.ModelSerializer):
    purchase=serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ['username', 'wallet','purchase']