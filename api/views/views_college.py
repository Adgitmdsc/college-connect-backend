from api.views.views import *
from api.serializers import serializers_college
from api.serializers import serializers_society

class college_all(APIView):
    serializer_class = serializers_college.college_serializer

    def get(self, request):
        serializer = self.serializer_class
        queryset = serializers_college.database_main_models.College.objects.all()
        serializer = serializer(queryset, many=True)
        return Response(serializer.data)

class college(APIView):

    def get(self, request, pk):
        serializer = serializers_college.college_serializer

        try:
            queryset = serializers_college.database_main_models.College.objects.get(id=pk)
            serializer = serializer(queryset, many=False)
            
            return Response(serializer.data)

        except serializers_college.database_main_models.College.DoesNotExist:
            return HttpResponse(status=404, content=b'College with this id does not exist')
            
        except Exception as exception:
            print(exception)
            return HttpResponse(status=500, content=b'Internal Server Error')

class college_societies(APIView):

    def get(self, request, pk):

        try:
            college = serializers_college.database_main_models.College.objects.get(id=pk)
            college_serializer = serializers_college.college_serializer(college, many=False)

            societies = serializers_society.database_main_models.Society.objects.filter(
                society_college = college
            )
            societies_serializer = serializers_society.society_serializer(societies, many=True)
            
            return Response({
                'college': college_serializer.data,
                'societies': societies_serializer.data
            })

        except serializers_college.database_main_models.College.DoesNotExist:
            return HttpResponse(status=404, content=b'College with this id does not exist')
            
        except Exception as exception:
            print(exception)
            return HttpResponse(status=500, content=b'Internal Server Error')