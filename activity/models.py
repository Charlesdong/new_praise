# -*- coding: utf-8 -*-
from django.db import models
from members.models import ChoirMembers


class Priest(models.Model):
    name = models.CharField(u'证道人', max_length=50)
    telephone = models.CharField(u'联系电话', max_length=20, blank=True, null=True)
    email = models.CharField(u'邮箱', max_length=100, blank=True, null=True)
    extra = models.TextField(u'其他联系方式', blank=True, null=True)

    class Meta:
        db_table = u'priest'

    def __unicode__(self):
        return self.name


class Songs(models.Model):
    name = models.CharField(u'歌曲名字', max_length=100)
    author = models.CharField(u'歌曲作者', max_length=300)
    mp3 = models.CharField(u'mp3链接', max_length=500, blank=True, null=True)
    musicbook = models.FileField(u'歌谱', upload_to='/home/upload/musicbook', max_length=500, blank=True, null=True)

    class Meta:
        db_table = u'songs'

    def __unicode__(self):
        return self.name


class CompereWeekly(models.Model):
    compers = models.ManyToManyField(ChoirMembers)
    compe_songs = models.ManyToManyField(Songs)
    compe_date = models.DateField(u'主礼日期')
    speaker = models.CharField(u'证道人', max_length=50, blank=True, null=True)
    verse = models.TextField(u'证道经文', blank=True, null=True)
    createtime = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        db_table = u'choir_weekly'

    def __unicode__(self):
        return self.name

