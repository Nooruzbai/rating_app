from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters

from school_rating.models import School
from school_rating.serializers.school_serializers import SchoolSerializer, SchoolDetailSerializer


class SchoolListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {'name': ['exact'],
                        'type': ['exact'],
                        'setting': ['exact'],
                        'tuition': ['gte', 'lte', 'exact', 'gt', 'lt']
                        }
    search_fields = ['name',
                     'type',
                     'setting',
                     'tuition'
                     ]


class SchoolCreateView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SchoolSerializer


class SchoolDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = School.objects.all()
    serializer_class = SchoolDetailSerializer


class SchoolUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = School.objects.all()
    serializer_class = SchoolDetailSerializer


class SchoolDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = School.objects.all()
    serializer_class = SchoolDetailSerializer
