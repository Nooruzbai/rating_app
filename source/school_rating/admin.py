from django.contrib import admin
from school_rating.models import School, Rating, SchoolRating, Comment, CommentLike


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'address', 'type', 'setting', 'webpage']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_created']


class SchoolRatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_id', 'rating_id', 'score', 'date_created']


class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'comment_id']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'school_id', 'date_created']


admin.site.register(School, SchoolAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(SchoolRating, SchoolRatingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentLike, CommentLikeAdmin)
