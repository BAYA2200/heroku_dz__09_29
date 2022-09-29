
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('categorys/', views.CategoryListCreateView.as_view()),
    path('categorys/<int:pk>', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('questions/', views.QuestionAnswerListCreateView.as_view()),
    path('questions/<int:pk', views.QuestionAnswerRetrieveUpdateDestroyAPIView.as_view()),
]
