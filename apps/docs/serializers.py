from rest_framework import serializers
from .models import ApiDoc, ApiDocSection

class ApiDocSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiDocSection
        fields = '__all__'

class ApiDocDetailSerializer(serializers.ModelSerializer):
    sections = ApiDocSectionSerializer(many = True)
    class Meta:
        model = ApiDoc
        fields = '__all__'

class ApiDocListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiDoc
        fields = ['id', 'title', 'slug', 'description', 'imgURL']