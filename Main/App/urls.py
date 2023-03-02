from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', OrderAPIView.as_view()),
    path('cart/<int:pk>/', OrderAPIView.as_view()),
]
