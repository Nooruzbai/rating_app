from django.urls import path

from school_rating.views.comment_views import CommentView, CommentDetailView
from school_rating.views.rating_views import RatingListView, RatingDetailView
from school_rating.views.school_views import SchoolListView, SchoolDetailView, SchoolCreateView, SchoolDeleteView, \
    SchoolUpdateView


app_name = 'school_rating'


urlpatterns = [
    path('schools/list/', SchoolListView.as_view(), name='schools_list_view'),
    path("school/create/", SchoolCreateView.as_view(), name='school_create_view'),
    path('school/detail/<int:pk>/', SchoolDetailView.as_view(), name='school_detail_view'),
    path('school/delete/<int:pk>/', SchoolDeleteView.as_view(), name='school_delete_view'),
    path('school/update/<int:pk>', SchoolUpdateView.as_view(), name='school_update_view'),

    path('ratings/list/', RatingListView.as_view(), name="rating_list_view"),
    path('rating/detail/<int:pk>/', RatingDetailView.as_view(), name="rating_detail_view"),


    path('comment/', CommentView.as_view(), name='comment_view'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment_detail_view')
]
