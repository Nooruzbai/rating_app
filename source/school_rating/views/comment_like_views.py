from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from school_rating.models import CommentLike
from school_rating.serializers.comment_like_serilizers import CommentLikeSerializer


class CreateCommentLike(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = CommentLikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        