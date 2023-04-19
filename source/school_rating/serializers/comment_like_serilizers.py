from rest_framework import serializers

from school_rating.models import CommentLike


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['comment_id', 'date_created']


