from django.contrib import admin
from school_rating.models import School, Rating, SchoolRating, Comment
# Register your models here.


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'type', 'address', 'setting', 'webpage']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_created']


class SchoolRatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'rating', 'score', 'date_created']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','text' ]

admin.site.register(School, SchoolAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(SchoolRating, SchoolRatingAdmin)
admin.site.register(Comment, CommentAdmin)