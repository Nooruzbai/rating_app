from django.urls import path
from school_rating.views import School_list_view

urlpatterns = [
    path('', School_list_view.as_view(), name='school_list_view'),
]
