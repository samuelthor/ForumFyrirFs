from django.db import models


class Post(models.Model):
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.post_text

class Comment(models.Model):
    post = models.ForeignKey(Question)
    comment_text = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.commnet_text
