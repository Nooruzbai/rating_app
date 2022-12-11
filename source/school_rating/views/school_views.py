from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from school_rating.models import School
from school_rating.serializers.school_serializers import SchoolSerializer, SchoolDetailSerializer


class SchoolListView(APIView):

    def get(self, request, format=None):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SchoolDetailView(APIView):
    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = SchoolDetailSerializer(school)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        school = self.get_object(pk)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
