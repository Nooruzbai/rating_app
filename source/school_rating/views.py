from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class School_list_view(APIView):
    def get(self, request, format=None):
        return Response(data={'greating': 'Hi Nooruzbai'})
