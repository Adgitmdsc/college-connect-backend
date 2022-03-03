from django.urls import path

from api.views import views_user

urlpatterns = [
    path('', views_user.user.as_view()),
    path('signup/', views_user.signup_user.as_view()),
    path('login/', views_user.login_user.as_view()),
]