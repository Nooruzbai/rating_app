from rest_framework import serializers
from school_rating.models import CommentLike


class SchoolCommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['comment', 'date_created']



