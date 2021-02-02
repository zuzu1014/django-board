from django.urls import path
from . import views

app_name = 'posts'


urlpatterns = [

    path('board/', views.BoardView.as_view()),
    
]
