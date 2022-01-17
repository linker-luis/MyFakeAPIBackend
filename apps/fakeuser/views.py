# from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import FakeUserSerializer, FakeUserDetailSerializer, FakeUserLoginSerializer
from .models import (
    FakeUser,
    Address,
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

            return Response({'key': token}, status = status.HTTP_200_OK)
        
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