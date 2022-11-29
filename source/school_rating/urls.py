from django.urls import path

from school_rating.views.rating_views import RatingListView, RatingDetailView
from school_rating.views.schoo_views import SchoolListView, SchoolDetailView

urlpatterns = [
    path('', SchoolListView.as_view(), name='school_list_view'),
    path('school/<int:pk>/', SchoolDetailView.as_view(), name='school_detail_view'),
    path('rating/', RatingListView.as_view(), name="rating_list_view"),
    path('rating/<int:pk>', RatingDetailView.as_view(), name="rating_detail_view"),
]
