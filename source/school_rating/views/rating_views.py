from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from school_rating.models import Rating
from school_rating.serializers.rating_serializers import RatingSerializer, RatingDetailSerializer


class RatingListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name',]


class RatingDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = RatingDetailSerializer
    queryset = Rating.objects.all()