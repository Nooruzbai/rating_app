from django.urls import path

from news.views import GetAllNewsView

app_name = 'news'

urlpatterns = [
    path('all/', GetAllNewsView.as_view(), name='news'),
]