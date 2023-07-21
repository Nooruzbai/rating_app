from rest_framework import serializers

from school_rating.models import Comment


class SchoolCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user_id', 'school_id', 'text', 'date_created',]


class SchoolCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['school', 'text']


class SchoolCommentDetailSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField('get_total_likes')

    class Meta:
        model = Comment
        fields = ['id', 'user_id', 'school_id', 'text', 'date_created', 'total_likes']

    def get_total_likes(self, obj):
        query = Comment.objects.get(id=obj.id).comment_likes.filter(comment_id=obj.id).count()
        return query



