from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from school_rating.models import Comment
from school_rating.serializers.comment_serializers import CommentSerializer


class CommentView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    @swagger_auto_schema(
        operation_summary="Adds a comment",
        operation_description="You need to send the current user_id, school_id, text"
    )
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CommentDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Gets the comment for detailed view.",
    )
    def get(self, request, pk, *args, **kwargs):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Edits the comment or if does not exist adds it.",
    )
    def put(self, request, pk, *args, **kwargs):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment,
                                      data=request.data,
                                      partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Deletes the comment.",
    )
    def delete(self, request, pk, *args, **kwargs):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

