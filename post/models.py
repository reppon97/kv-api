from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, db_index=True)
    content = models.TextField(max_length=500, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    # image = models.ImageField(upload_to='post_images/', null=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commented_post')
    content = models.TextField(max_length=250, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author', db_index=True)
    # attached_image = models.ImageField(upload_to='attached_images/', null=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ('-created',)

    def __str__(self):
        return self.content


# class Reply(models.Model):
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replied_comments')
#     content = models.CharField(max_length=250, null=False)
#     # attached_image = models.ImageField(upload_to='reply_images/', null=True)
#     attachment = models.FileField(upload_to='attachments/', null=True)
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = 'Replies'
#         ordering = ('-created',)
#
#     def __str__(self):
#         return self.content
