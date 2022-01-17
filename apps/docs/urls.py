from django.urls import path
from .views import ApiDocDetailAPIView, ApiDocListAPIView

urlpatterns = [
    path('api/docs/', ApiDocListAPIView.as_view()),
    path('api/docs/<slug>/', ApiDocDetailAPIView.as_view())
]