from rest_framework import generics
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .filters import ProductFilter
from .serializers import (
    ProductSerializer,
    SimpleProductSerializer,
    CartSerializer,
    categorySerializer
)
from apps.fakeuser.models import FakeUser
from .models import (
    Cart,
    Category,
    Product
)

class ProductListAPIView(generics.ListAPIView):
    serializer_class = SimpleProductSerializer
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
    # filterset_fields = ('category__name__iexact', 'name')

class FeaturedProductAPIView(generics.ListAPIView):
    serializer_class = SimpleProductSerializer
    queryset = Product.objects.all().order_by('?')[:5]

class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'

# cart

class CartListAPIView(generics.ListAPIView):
    serializer_class = CartSerializer
    # queryset = Cart.objects.all()

    def get_queryset(self):
        
        try:
            req = self.request.META['HTTP_AUTHORIZATION']            
            token = req.split()
            fake_user = FakeUser.objects.get(token__key =  token[1])
            # print(token, fake_user, fake_user.exists())
            
            return Cart.objects.filter(user = fake_user)
            
            
        except:              
            # print('no req')
            return Cart.objects.all()

class CartDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    lookup_field = 'id'

# categories

class CategoryListAPIView(generics.ListAPIView):
    serializer_class = categorySerializer
    queryset = Category.objects.all()