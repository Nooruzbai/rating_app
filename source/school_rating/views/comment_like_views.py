from django.http import Http404
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from school_rating.models import CommentLike
from school_rating.serializers.comment_like_serilizers import CommentLikeSerializer


class CreateCommentLike(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = CommentLikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = self.request.user
            comment_id = self.request.data.get('comment')
            try:
                query = get_object_or_404(CommentLike, user_id=user, comment_id=comment_id)
            except Http404:
                serializer.save(user=self.request.user)
                message = {"message": f"You liked the comment {comment_id}"}
                return Response(message, status=status.HTTP_201_CREATED)
            else:
                query.delete()
                message = {"message": f"You unliked the comment {comment_id}"}
                return Response(message, status=status.HTTP_201_CREATED)