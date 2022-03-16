from django.urls import path

from api.views import views_college

urlpatterns = [
    path('', views_college.college_all.as_view()),
    path('<int:pk>/', views_college.college.as_view()),
    path('<int:pk>/societies/', views_college.college_societies.as_view()),
]