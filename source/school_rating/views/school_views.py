from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from school_rating.models import School
from school_rating.serializers.school_serializers import SchoolSerializer, SchoolDetailSerializer



class SchoolListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]

    @swagger_auto_schema(
        operation_summary="Gets and lists all the schools.",
    )
    def get(self, request, *args, **kwargs):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Creates a new school.",
    )
    def post(self, request,  *args, **kwargs):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SchoolDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Gets the school for detailed view.",
    )
    def get(self, request, pk, *args, **kwargs):
        school = self.get_object(pk)
        serializer = SchoolDetailSerializer(school)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_summary="Edits the school.",
    )
    def put(self, request, pk, *args, **kwargs):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Deletes the school.",
    )
    def delete(self, request, pk, *args, **kwargs):
        school = self.get_object(pk)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
