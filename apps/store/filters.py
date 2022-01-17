from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    # name_filter = filters.CharFilter(field_name = 'name', lookup_expr = 'icontains')
    name = filters.CharFilter(lookup_expr = 'icontains')

    class Meta:
        model = Product
        fields = ['category__name', 'name']