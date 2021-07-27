from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, db_index=True)
    content = models.TextField(max_length=500, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    image = models.ImageField(upload_to='post_images/', null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=250, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author', db_index=True)
    attached_image = models.ImageField(upload_to='attached_images/', null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ('-created',)

    def __str__(self):
        return self.content


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.CharField(max_length=250, null=False)
    attached_image = models.ImageField(upload_to='reply_images/', null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Replies'
        ordering = ('-created',)

    def __str__(self):
        return self.content
