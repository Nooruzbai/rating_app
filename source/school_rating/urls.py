from django.urls import path
from school_rating.views import SchoolListView

urlpatterns = [
    path('', SchoolListView.as_view(), name='school_list_view'),
]
