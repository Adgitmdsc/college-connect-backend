from django.urls import path, include

urlpatterns = [
    path('user/', include('api.urls.urls_user')),
    path('college/', include('api.urls.urls_college')),
]