from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from school_rating.models import CommentLike
from school_rating.serializers.comment_like_serilizers import CommentLikeSerializer


class CreateCommentLike(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = CommentLikeSerializer

    def perform_creat(self, serializer):
        serializer.save(user_id=self.request.user.id)

    # def get_queryset(self):
    #     user = self.request.user
    #     comment = self.request.GET.get('comment_id')
    #     print(comment)
    #     found_comment = CommentLike.comment_id.objects.filter(comment)
    #     print(found_comment)
