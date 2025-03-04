from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListCreateAPIView,ListAPIView
from rest_framework import authentication, permissions
from tracker.serializers import UserCreationSerializer,MealSerializer
from tracker.models import Meal
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response


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


class TotalCalorieView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):

        total_sum=Meal.objects.filter(user=request.user).values("calories").aggregate(total=Sum("calories"))
        return Response(data=total_sum)

