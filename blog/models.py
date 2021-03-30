from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_date = models.DateTimeField(default=timezone.now)
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return ("[ " + str(self.post_date) + " ] " + self.post_title)