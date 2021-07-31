# Kvartirka REST API Task

## Implementation of Kvartirka task.

-----------------------

### Usage


```make docker-init```

It migrates the models, creates superuser and seeds 100 dummy users, posts, comments and replies.

superuser username: admin

superuser password: password123

## To Run:

```make docker-up```

## Useful Links:
[Posts APIView](http://0.0.0.0:8000/post)

[Post DetailView](http://0.0.0.0:8000/post/detail/<post_id>)

[Comments APIView](http://0.0.0.0:8000/post/comments/)

[Comment DetailView](http://0.0.0.0:8000/post/comments/detail/<comment_id>)

[Reply APIView](http://0.0.0.0:8000/post/replies/)

[Reply DetailView](http://0.0.0.0:8000/post/replies/detail/<reply_id>)
