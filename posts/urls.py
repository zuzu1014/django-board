from django.urls import path
from . import views

app_name = 'posts'


urlpatterns = [
    path('board/scroll/', views.BoardScrollView.as_view()),
]
