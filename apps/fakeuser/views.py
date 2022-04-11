# from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import (
    FakeUserSerializer, 
    FakeUserDetailSerializer, 
    FakeUserLoginSerializer,
    SimplePersonalInformationSerializer,
    PersonalInformationSerializer
    # CreateFakeUserListSerializer
)
from .models import (
    FakeUser,
    Location,
    PersonalInformation,
    FakeToken,
    
)

class FakeUserListAPIView(generics.ListAPIView):
    serializer_class = FakeUserSerializer
    queryset = FakeUser.objects.all()

class FakeUserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = FakeUserDetailSerializer
    queryset = FakeUser.objects.all()
    lookup_field = 'id'

@api_view(['POST'])
def fakeLoginAPIView(request):
    data = request.data
    serializer = FakeUserLoginSerializer(data = data)

    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        try:
            fake_user = FakeUser.objects.get(username = username, password = password)
            token = fake_user.token.key
            first_name = fake_user.personal_information.first_name
            img = fake_user.personal_information.img

            return Response({
                'key': token, 
                'person_data': {
                    'id': fake_user.id, 
                    'username': fake_user.username, 
                    'first_name': first_name, 
                    'img': img}
                }, status = status.HTTP_200_OK)
        
        except:

            return Response({'message': 'Los datos son incorrectos'}, status = status.HTTP_400_BAD_REQUEST)

        # print('funciona')
        # return Response({'username': username, 'password': password}, status= status.HTTP_200_OK)
        # # fake_user = FakeUser.objects.get()

    return Response({'message': 'error al logear'}, status = status.HTTP_400_BAD_REQUEST)

# {
# "username": "sdgsdg",
# "password": "dsfsdf"
# }

@api_view(['POST'])
def fake_logout(request):
    # print(request.META)
    # print(request.META['HTTP_AUTORIZATION'])
    return Response({'message': 'Success Logout'}, status= status.HTTP_200_OK)


# personal information

class PersonListApiView(generics.ListAPIView):
    serializer_class = SimplePersonalInformationSerializer
    queryset = PersonalInformation.objects.all()

class PersonDetailApiView(generics.RetrieveAPIView):
    serializer_class = PersonalInformationSerializer
    queryset = PersonalInformation.objects.all()
    lookup_field = 'id'

# only for admin

# class CreateFakeUserListView(APIView, ListModelMixin, CreateModelMixin):
#     serializer_class = CreateFakeUserListSerializer
#     queryset = FakeUser.objects.all()
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]