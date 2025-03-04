from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListCreateAPIView,ListAPIView
from rest_framework import authentication, permissions
from tracker.serializers import UserCreationSerializer,MealSerializer
from tracker.models import Meal

class UserCreateView(CreateAPIView):
    serializer_class = UserCreationSerializer


class MealListCreateView(ListAPIView, CreateAPIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MealSerializer

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

