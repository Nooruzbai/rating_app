from django.http import Http404
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from school_rating.models import SchoolLike
from school_rating.serializers.school_serializers import SchoolLikeSerializer


class SchoolLikeView(CreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SchoolLikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_id = self.request.user
            school_id = self.request.data.get('school_id')
            try:
                query = get_object_or_404(SchoolLike, user_id=user_id, school_id=school_id)
            except Http404:
                serializer.save(user_id=self.request.user)
                message = {"message": f"You liked the school {school_id}"}
                return Response(message, status=status.HTTP_201_CREATED)
            else:
                query.delete()
                message = {"message": f"You unliked the school {school_id}"}
                return Response(message, status=status.HTTP_201_CREATED)


