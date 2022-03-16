from api.serializers.serializers import *
from database_main import models as database_main_models

class society_serializer(serializers.ModelSerializer):
	class Meta:
		model = database_main_models.Society
		fields = (
            'id',
            'society_name',
            'society_identifier'
        )