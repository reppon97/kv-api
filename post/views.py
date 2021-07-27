from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from post.models import Post, Comment, Reply
from post.serializer import PostSerializer, CommentSerializer, ReplySerializer


def add(request):
    if request.method == 'POST':
        data = request.params
        post = Post(title=data['title'], content=data['content'],
                    author=request.user, image=data['image'])


class PostView(APIView):
    @staticmethod
    def get(request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):
    @staticmethod
    def get(request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyView(APIView):
    @staticmethod
    def get(request):
        replies = Reply.objects.all()
        serializer = ReplySerializer(replies, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = ReplySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
