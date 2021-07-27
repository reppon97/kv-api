from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('', views.PostView.as_view()),
    path('comment/', views.CommentView.as_view()),
    path('reply/', views.ReplyView.as_view()),
]
