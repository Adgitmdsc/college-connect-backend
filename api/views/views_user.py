from api.views.views import *
from api.serializers import serializers_user
from rest_framework.authtoken.models import Token

class user(APIView):
    serializer_class = serializers_user.user_serializer

    def get(self, request):
        serializer = self.serializer_class
        queryset = serializers_user.database_user_models.User.objects.all()
        serializer = serializer(queryset, many=True)
        return Response(serializer.data)

class signup_user(APIView):
    serializer_class = serializers_user.signup_user_serializer

    def post(self, request):
        instance = self.serializer_class(data=request.data)
        instance.is_valid(raise_exception=True)
        instance = instance.save()

        if instance != None:
            return Response({
                "user": serializers_user.user_serializer(instance).data,
                "token": Token.objects.get_or_create(user=instance)[0].__str__()
            })
        else:
            return Response({
                "msg": "Internal Server Error"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class login_user(APIView):
    serializer_class = serializers_user.login_user_serializer

    def post(self, request):
        from django.contrib.auth import authenticate
        instance = authenticate(username=request.data['username'], password=request.data['password'])

        if instance != None:
            return Response({
                "account": serializers_user.user_serializer(instance).data,
                "token": Token.objects.get_or_create(user=instance)[0].__str__()
            })
        else:
            return Response({
                "msg": "Wrong Credentials"
            }, status=status.HTTP_401_UNAUTHORIZED)