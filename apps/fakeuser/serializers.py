from rest_framework import serializers
from .models import (
    FakeToken,
    FakeUser,
    Address,
    PersonalInformation
)

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = ['id', 'city', 'street', 'zip_code']

class PersonalInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalInformation
        fields = ['id', 'name', 'lastname', 'phone']

class FakeUserDetailSerializer(serializers.ModelSerializer):
    personal_information = PersonalInformationSerializer()
    address = AddressSerializer()

    class Meta:
        model = FakeUser
        fields = ['id', 'username', 'email', 'password', 'personal_information', 'address']

class FakeUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FakeUser
        fields = ['id', 'username', 'email', 'password']

class FakeUserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = FakeUser
        fields = ['username', 'password']