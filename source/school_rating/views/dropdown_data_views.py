from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
@swagger_auto_schema(operation_description="Receives all cities")
def get_school_cities_view(request):
        content = {
            "0": "Not Assigned",
            "1": "Bishkek",
            "2": "Naryn",
            "3": "Karakol",
            "4": "Osh",
            "5": "Jalal-Abad",
            "6": "Batken",
            "7": "Talas",
        }
        return Response(content)


@api_view(['GET'])
@swagger_auto_schema(operation_description="Receives all settings")
def get_school_setting_view(request):
    content = {
        "0": "Not Assigned",
        "1": "City",
        "2": "Suburb",
        "3": "Village",
    }

    return Response(content)


@api_view(['GET'])
@swagger_auto_schema(operation_description="Receives all types")
def get_school_type_view(request):
    content = {
        "0": "Not Assigned",
        "1": "Public",
        "2": "Private",
        "3": "Non Commercial"
    }

    return Response(content)



