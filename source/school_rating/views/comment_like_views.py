from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from school_rating.models import CommentLike
from school_rating.serializers.comment_like_serilizers import CommentLikeSerializer


class CreateCommentLike(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = CommentLikeSerializer

    def perform_create(self, serializer):
        if self.get_queryset():
            return f"Like already exists"
        serializer.save(user=self.request.user)

    def get_queryset(self):
        likes = CommentLike.objects.filter(user_id=self.request.user)
        return likes
