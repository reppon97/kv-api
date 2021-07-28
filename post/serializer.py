from rest_framework.serializers import ModelSerializer

from post.models import Post, Comment


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

#
# class ReplySerializer(ModelSerializer):
#     class Meta:
#         model = Reply
#         fields = "__all__"
