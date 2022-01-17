from django.urls import path
from .views import (
    FakeUserListAPIView,
    FakeUserDetailAPIView,
    fakeLoginAPIView,
    fake_logout,
)

urlpatterns = [
    path('api/get_users/', FakeUserListAPIView.as_view(), name = 'get_users'),
    path('api/get_users/<int:id>/', FakeUserDetailAPIView.as_view(), name = 'user_details'),
    path('api/user_login/', fakeLoginAPIView, name= 'fakelogin'),
    path('api/user_logout/', fake_logout, name= 'fake_logout')

]