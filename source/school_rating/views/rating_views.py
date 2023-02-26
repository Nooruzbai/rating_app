from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from school_rating.models import Rating
from school_rating.serializers.rating_serializers import RatingSerializer, RatingDetailSerializer


class RatingListView(APIView):

    @swagger_auto_schema(
        operation_summary="Gets and lists all the ratings.",
    )
    def get(self, request,  args, **kwargs):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Creates a rating",
    )
    def post(self, request, args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RatingDetailView(APIView):

    def get_object(self, pk):
        try:
            return Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Gets the rating for detailed view",
    )
    def get(self, request, pk, format=None):
        rating = self.get_object(pk)
        serializer = RatingDetailSerializer(rating)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_summary="Edits the rating",
    )
    def put(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = RatingSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = RatingSerializer(school,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Deletes the rating",
    )
    def delete(self, request, pk, format=None):
        school = self.get_object(pk)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)