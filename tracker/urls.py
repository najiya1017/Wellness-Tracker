from django.urls import path
from tracker import views


urlpatterns = [
    path("create/",views.UserCreateView.as_view()),
    path("meals/", views.MealListCreateView.as_view()),
    path("calorie/sum/",views.TotalCalorieView.as_view()),
]
