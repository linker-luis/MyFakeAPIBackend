from rest_framework import serializers
from .models import (
    FakeToken,
    FakeUser,
    Location,
    PersonalInformation
)

class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Location
        fields = [
            'id', 
            'country',
            'city', 
            'street', 
            'street_number',
            'zip_code'
        ]

class SimplePersonalInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalInformation
        fields = [
            'id',
            'first_name',
            'last_name',
            'img',
            'phone',
            'email',
            'job_title'
        ]

class PersonalInformationSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = PersonalInformation
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'img',
            'phone',
            'email', 
            'gender',
            'gender_abbrev',
            'job_title',
            'location'
        ]

class FakeUserDetailSerializer(serializers.ModelSerializer):
    personal_information = PersonalInformationSerializer()
    
    class Meta:
        model = FakeUser
        fields = ['id', 'username', 'email', 'password', 'personal_information']

class FakeUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FakeUser
        fields = ['id', 'username', 'email', 'password']

class FakeUserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = FakeUser
        fields = ['username', 'password']





# class PersonDetailSerialiser(serializers.ModelSerializer):

#     class Meta: 
#         model = PersonalInformation
#         fields = [

#         ]

#for admin

# class CreateFakeUserListSerializer(serializers.ModelSerializer):
#     personal_information = PersonalInformationSerializer()
    
#     class Meta:
#         model = FakeUser
#         fields = ['id', 'username', 'email', 'password', 'personal_information']

    # def create(self, validated_data):
    #     fake1 = FakeUser.objects.all()

    #     print(validated_data)

    #     return fake1

# class CreateFakeUserListSerializer(serializers.Serializer):
#     fake_users = serializers.ListField(
#         child = FakeUserDetailSerializer()
#     )


# [
#     {
#         "id": 1,
#         "username": "pruebaedgdr",
#         "email": "sdvsd@gmil.com",
#         "password": "19a6sd65",
#         "personal_information": {
#             "id": 1,
#             "first_name": "Camilla",
#             "last_name": "D'Ruel",
#             "phone": "347575694",
#             "email": "sdv@gmil.com",
#             "gender": "Female",
#             "gender_abbrev": "F",
#             "job_title": "Database Administrator II",
#             "location": {
#                 "id": 1,
#                 "country": "United States",
#                 "city": "Clearwater",
#                 "street": "Talisman",
#                 "street_number": "94",
#                 "zip_code": "46857"
#             }
#         }
#     },
#     {
#         "id": 1,
#         "username": "pruebdffaer",
#         "email": "sdv@gmil.com",
#         "password": "19yy6655",
#         "personal_information": {
#             "id": 1,
#             "first_name": "Camilla",
#             "last_name": "D'Ruel",
#             "phone": "347575694",
#             "email": "sdv@gmil.com",
#             "gender": "Female",
#             "gender_abbrev": "F",
#             "job_title": "Database Administrator II",
#             "location": {
#                 "id": 1,
#                 "country": "United States",
#                 "city": "Clearwater",
#                 "street": "Talisman",
#                 "street_number": "94",
#                 "zip_code": "46857"
#             }
#         }
#     }
# ]