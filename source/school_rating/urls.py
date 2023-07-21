from django.urls import path

from school_rating.views.comment_like_views import CreateSchoolCommentLikeView
from school_rating.views.comment_views import SchoolCommentListView, SchoolCommentCreateView, SchoolCommentDetailView, \
    SchoolCommentDeleteView, SchoolCommentUpdateView
from school_rating.views.dropdown_data_views import get_school_cities_view, get_school_setting_view, \
    get_school_type_view
from school_rating.views.rating_views import RatingListView, RatingDetailView
from school_rating.views.school_like_views import SchoolLikeView
from school_rating.views.school_views import SchoolListView, SchoolDetailView, SchoolCreateView, SchoolDeleteView, \
    SchoolUpdateView

app_name = 'school_rating'


urlpatterns = [
    path('schools/list/', SchoolListView.as_view(), name='schools_list_view'),
    path('school/create/', SchoolCreateView.as_view(), name='school_create_view'),
    path('school/detail/<int:pk>/', SchoolDetailView.as_view(), name='school_detail_view'),
    path('school/delete/<int:pk>/', SchoolDeleteView.as_view(), name='school_delete_view'),
    path('school/update/<int:pk>', SchoolUpdateView.as_view(), name='school_update_view'),

    path('ratings/list/', RatingListView.as_view(), name="rating_list_view"),
    path('rating/detail/<int:pk>/', RatingDetailView.as_view(), name="rating_detail_view"),


    path('school/like/', SchoolLikeView.as_view(), name='school_like_view'),


    path('school/comments/list/', SchoolCommentListView.as_view(), name='comment_list_view'),
    path('school/comment/create/', SchoolCommentCreateView.as_view(), name='comment_create'),
    path('school/comment/detail/<int:pk>/', SchoolCommentDetailView.as_view(), name='comment_detail_view'),
    path('school/comment/delete/<int:pk>/', SchoolCommentDeleteView.as_view(), name='comment_delete_view'),
    path('school/comment/update/<int:pk>', SchoolCommentUpdateView.as_view(), name='comment_update_view'),

    path('school/comment/like/', CreateSchoolCommentLikeView.as_view(), name='school_comment_like_view'),

    path('school/get_cities', get_school_cities_view, name='get_cities'),
    path('school/get_settings', get_school_setting_view, name='school_settings'),
    path('school/get_types', get_school_type_view, name='school_types'),


]
