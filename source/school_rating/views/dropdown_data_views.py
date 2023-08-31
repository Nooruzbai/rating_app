from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
@swagger_auto_schema(operation_description="Receives all cities")
def get_school_cities_view(request):
        content = [
            {"id": 0, "name": "Not Assigned"},
            {"id": 1, "name": "Bishkek"},
            {"id": 2, "name": "Naryn"},
            {"id": 3, "name": "Karakol"},
            {"id": 4, "name": "Osh"},
            {"id": 5, "name": "Jalal-Abad"},
            {"id": 6, "name": "Batken"},
            {"id": 7, "name": "Talas"},
            {"id": 8, "name": "Bishkek"}
        ]
        return Response(content)


@api_view(['GET'])
@swagger_auto_schema(operation_description="Receives all settings")
def get_school_setting_view(request):
    content = [
        {"id": 0, "name": "Not Assigned"},
        {"id": 1, "name": "City"},
        {"id": 2, "name": "Suburb"},
        {"id": 3, "name": "Village"},
    ]
    return Response(content)


@api_view(['GET'])
@swagger_auto_schema(operation_description="Receives all types")
def get_school_type_view(request):
    content = [
        {"id": 0, "name": "Not Assigned"},
        {"id": 1, "name": "Public"},
        {"id": 2, "name": "Private"},
        {"id": 3, "name": "Non Commercial"},
    ]
    return Response(content)



