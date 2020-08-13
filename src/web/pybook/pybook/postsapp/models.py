from django.db import models


class Post(models.Model):
    body = models.TextField()
    user = models.TextField()
    datetime = models.DateTimeField()

    def __str__(self):
        return self.body
