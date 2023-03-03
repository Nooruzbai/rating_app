from django.urls import path

from school_rating.views.comment_views import CommentView
from school_rating.views.rating_views import RatingListView, RatingDetailView
from school_rating.views.school_views import SchoolListView, SchoolDetailView


app_name = 'school_rating'

urlpatterns = [
    path('schools', SchoolListView.as_view(), name='school_list_view'),
    path('school/<int:pk>', SchoolDetailView.as_view(), name='school_detail_view'),
    path('ratings', RatingListView.as_view(), name="rating_list_view"),
    path('rating/<int:pk>', RatingDetailView.as_view(), name="rating_detail_view"),
    path('comment/', CommentView.as_view(), name='comment_view')
]
