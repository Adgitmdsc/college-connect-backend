from django.urls import path, include

urlpatterns = [
    path('user/', include('api.urls.urls_user'))
]