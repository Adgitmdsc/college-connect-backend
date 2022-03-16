from api.serializers.serializers import *
from database_main import models as database_main_models

class college_serializer(serializers.ModelSerializer):
	class Meta:
		model = database_main_models.College
		fields = (
            'id',
            'college_name',
            'college_identifier'
        )