from rest_framework import generics
from .serializers import ApiDocDetailSerializer, ApiDocListSerializer
from .models import ApiDoc

class ApiDocDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ApiDocDetailSerializer
    queryset = ApiDoc.objects.all() 
    lookup_field = 'slug'

class ApiDocListAPIView(generics.ListAPIView):
    serializer_class = ApiDocListSerializer
    queryset = ApiDoc.objects.all()
