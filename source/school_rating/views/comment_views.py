from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, \
                                    UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from school_rating.models import Comment
from school_rating.serializers.comment_serializers import SchoolCommentSerializer,SchoolCommentCreateSerializer, \
                                                            SchoolCommentDetailSerializer


class SchoolCommentListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = SchoolCommentSerializer
    queryset = Comment.objects.all()


class SchoolCommentCreateView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = SchoolCommentCreateSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SchoolCommentDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = SchoolCommentDetailSerializer
    queryset = Comment.objects.all()


class SchoolCommentUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = SchoolCommentSerializer
    queryset = Comment.objects.all()


class SchoolCommentDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = SchoolCommentSerializer
    queryset = Comment.objects.all()
