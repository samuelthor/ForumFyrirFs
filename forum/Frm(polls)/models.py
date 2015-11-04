import datetime
from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.post_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment_text = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.commnet_text
