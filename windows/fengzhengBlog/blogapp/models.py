#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class fz_user(models.Model):
    displayname = models.CharField(max_length=56)
    loginname = models.CharField(max_length=56)
    password = models.CharField(max_length=128)
    user_email = models.EmailField(blank=True)
    user_status = models.BooleanField()
    registered_date = models.DateField()

    def __unicode__(self):
        return self.displayname

class fz_classic(models.Model):
    name = models.CharField(max_length=56)
    articecount = models.IntegerField()

    def __unicode__(self):
        return self.name




class fz_Article(models.Model):
    title = models.CharField(max_length=56,verbose_name='标题')
    content = models.TextField(verbose_name='文章内容')
    author = models.ForeignKey(fz_user)
    tags = models.CharField(max_length=1023,verbose_name='标签',blank=True)
    classic = models.ForeignKey(fz_classic)
    publish_date = models.DateTimeField()
    ispublished = models.BooleanField()
    commentcount = models.IntegerField(blank=True)
    readcount = models.IntegerField(blank=True)

class fz_comment(models.Model):
    article = models.ForeignKey(fz_Article)
    comment_content = models.TextField()
    comment_date = models.DateField()
    email = models.EmailField()
    commentator = models.TextField()