# -*- coding: utf-8 -*-
from django.db import models

GENDER_CHOICES = (
    (0, u'男'),
    (1, u'女')
)


class ChoirMembers(models.Model):
    name = models.CharField(u'姓名', max_length=200)
    gender = models.IntegerField(u'性别', choices=GENDER_CHOICES, default=0)
    native_place = models.CharField(u'籍贯', max_length=20, blank=True, null=True)
    telephone = models.CharField(u'联系电话', max_length=20, null=True, blank=True)
    qq = models.CharField(u'qq', max_length=20, blank=True, null=True)
    join_time = models.DateField(u'加入诗班时间', blank=True, null=True)
    baptize_time = models.DateField(u'受洗时间', blank=True, null=True)
    extra = models.TextField(u'备注',  blank=True, null=True)
    createtime = models.DateTimeField(u'创建时间', auto_now_add=True)
    updatetime = models.DateTimeField(u'更新时间', auto_now=True)

    class Meta:
        db_table = u'choir_members'

    def __unicode__(self):
        return self.name