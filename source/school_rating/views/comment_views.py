from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from school_rating.models import Comment
# from school_rating.models import Comment
from school_rating.serializers.comment_serializers import CommentSerializer, CreateCommentSerializer


class CommentListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentCreateView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = CreateCommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
