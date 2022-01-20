from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import SerializerMethodField
from .models import (
    Category,
    Product,
    Images,
    Cart,
    CartItem
)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = [
            # 'img', #--------------
            'imgURL'
            ]

class ProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many = True)
    category = CategorySerializer()

    class Meta: 
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'images'
        ]

# cart ========================================

class SimpleProductSerializer(serializers.ModelSerializer):
    # images = ImagesSerializer(many = True)
    # category = CategorySerializer()
    # image_url = SerializerMethodField()
    imageURL = SerializerMethodField()

    class Meta: 
        model = Product
        fields = [
            'id',
            'name',
            'price',
            # 'category',
            # 'image_url',
            'imageURL'
        ]

    # def get_image_url(self, obj):
    #     request = self.context.get('request')
    #     img = obj.images.all()[0]
    #     # print(img)
    #     return request.build_absolute_uri(img.img.url)

    def get_imageURL(self, obj):
        img = obj.images.all()[0]
        # print(img.imgURL)
        return img.imgURL
        

class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    # product_id = SerializerMethodField(read_only = True)

    class Meta:
        model = CartItem
        fields = [
            # 'id',
            # 'product_id',
            'product',
            'quantity'
        ]

    # def get_product_id(self, obj):
    #     product_id = obj.product.id
    #     return product_id

class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(many = True)
    user_id = SerializerMethodField(read_only = True)

    class Meta:
        model = Cart
        fields = [
            'id',
            'user_id',
            'products',
            'get_total_price',
            'get_total_quantity'
        ]
    
    def get_user_id(self, obj):
        user_id = obj.user.id
        return user_id


# https://learn.co/lessons/javascript-fetch

# categories

class categorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']

