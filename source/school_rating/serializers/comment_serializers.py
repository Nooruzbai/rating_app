from rest_framework import serializers

from school_rating.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'school', 'text', 'date_created']

class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['school', 'text']

