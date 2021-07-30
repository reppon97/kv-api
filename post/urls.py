from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('', views.PostAPIView.as_view()),
    path('detail/<int:pk>', views.PostDetailView.as_view()),
    path('comments/', views.CommentAPIView.as_view()),
    path('comments/detail/<int:pk>', views.CommentDetailView.as_view()),
    path('replies/', views.ReplyAPIView.as_view()),
    path('replies/detail/<int:pk>', views.ReplyDetailView.as_view()),
]
