from django.urls import path
from .views import (
    ProductListAPIView,
    FeaturedProductAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CartDetailAPIView,
    CartListAPIView,
)

urlpatterns = [
    path('api/products/', ProductListAPIView.as_view()),
    path('api/products/<int:id>/', ProductDetailAPIView.as_view()),
    path('api/featured_products/', FeaturedProductAPIView.as_view()),
    path('api/categories/', CategoryListAPIView.as_view()),
    path('api/carts/', CartListAPIView.as_view()),
    path('api/carts/<int:id>/', CartDetailAPIView.as_view())
]