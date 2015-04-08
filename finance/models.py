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
    devote_time = models.DateField(u'变更时间')
    createtime = models.DateTimeField(u'创建时间', auto_now_add=True)
    updatetime = models.DateTimeField(u'更新时间', auto_now=True)
    extra = models.TextField(u'备注', blank=True, null=True)

    class Meta:
        db_table = u'choir_finances'
        verbose_name = u'财务'
        verbose_name_plural = u'财务'

    def __unicode__(self):
        return self.operation