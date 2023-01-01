from django.urls import path

from news.views import GetAllNewsView

app_name = 'accounts'

urlpatterns = [
    path('all/', GetAllNewsView.as_view(), name='news'),
]