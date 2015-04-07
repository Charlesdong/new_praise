# -*- coding: utf-8 -*-
from django.db import models
from members.models import ChoirMembers


class SumFinances(models.Model):
    money = models.FloatField(u'总金额', default=0.00)

    class Meta:
        db_table = u'choir_sum'

    def __unicode__(self):
        return self.money


FINANCES_CHOICES = (
    (1, u'收入'),
    (0, u'支出'),
)

DEVOTION_CHOICES = (
    (1, u'是'),
    (0, u'否'),
)


class ChoirFinances(models.Model):
    member = models.ForeignKey(ChoirMembers)
    money = models.FloatField(u'金额', default=0.00)
    operation = models.IntegerField(u'操作', choices=FINANCES_CHOICES, default=0)
    is_devote = models.IntegerField(u'是否为奉献', choices=DEVOTION_CHOICES, default=0)
    sum = models.OneToOneField(SumFinances)
    extra = models.CharField(u'备注', max_length=500)
    devote_time = models.DateField(u'奉献时间')
    createtime = models.DateTimeField(u'创建时间', auto_now_add=True)
    updatetime = models.DateTimeField(u'更新时间', auto_now=True)

    class Meta:
        db_table = u'choir_finances'

    def __unicode__(self):
        return self.operation