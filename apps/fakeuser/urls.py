from django.urls import path
from .views import (
    FakeUserListAPIView,
    FakeUserDetailAPIView,
    fakeLoginAPIView,
    fake_logout,

    PersonListApiView,
    PersonDetailApiView,

    # CreateFakeUserListView
)

urlpatterns = [
    path('api/get_users/', FakeUserListAPIView.as_view(), name = 'get_users'),
    path('api/get_users/<int:id>/', FakeUserDetailAPIView.as_view(), name = 'user_details'),
    path('api/user_login/', fakeLoginAPIView, name= 'fakelogin'),
    path('api/user_logout/', fake_logout, name= 'fake_logout'),

    # person

    path('api/get_person/', PersonListApiView.as_view(), name = 'get_person'),
    path('api/get_person/<int:id>/', PersonDetailApiView.as_view(), name ='person_detail')

    # path('api/create_fakeuser_admin/', CreateFakeUserListView.as_view(), name = 'create_fakeusers_admin')

]