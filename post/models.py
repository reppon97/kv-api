from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, db_index=True)
    content = models.TextField(max_length=500, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commented_post')
    content = models.TextField(max_length=250, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author', db_index=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ('-created',)

    def __str__(self):
        return self.content


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replied_comments')
    content = models.TextField(max_length=250, null=False, blank=False)
    attachment = models.FileField(upload_to='attachments/', null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Replies'
        ordering = ('-created',)

    def __str__(self):
        return self.content
