from api.serializers.serializers import *
from database_user import models as database_user_models

class user_serializer(serializers.ModelSerializer):
	class Meta:
		model = database_user_models.User
		fields = ('id', 'username', 'email')

class signup_user_serializer(serializers.ModelSerializer):
	class Meta:
		model = database_user_models.User
		fields = ('id', 'username', 'email', 'password')
		extra_kwargs = {
            'password': {'write_only': True}
        }

	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save()
		return instance

class login_user_serializer(serializers.ModelSerializer):
	class Meta:
		model = database_user_models.User
		fields = ('username', 'password')
		extra_kwargs = {
            'password': {'write_only': True}
        }