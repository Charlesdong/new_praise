# -*- coding: utf-8 -*-
from django.db import models
from members.models import ChoirMembers


class TotalMoney(models.Model):
    total_money = models.FloatField(u'总金额', default=0.0)
    createtime = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        db_table = u'choir_finances_total'
        verbose_name = u'总金额'
        verbose_name_plural = u'总金额'

    def __unicode__(self):
        return str(self.total_money)


FINANCES_CHOICES = (
    (1, u'收入'),
    (0, u'支出'),
)

DEVOTION_CHOICES = (
    (0, u'聚餐'),
    (1, u'奉献'),
    (2, u'日常费用'),
    (3, u'其他'),
)


class ChoirFinances(models.Model):
    member = models.ForeignKey(ChoirMembers, verbose_name=u'成员')
    money = models.FloatField(u'金额', default=0.00)
    operation = models.IntegerField(u'操作', choices=FINANCES_CHOICES, default=0)
    event = models.IntegerField(u'事件', choices=DEVOTION_CHOICES, default=0)
    devote_time = models.DateField(u'时间')
    total_money = models.OneToOneField(TotalMoney, blank=True, null=True)
    createtime = models.DateTimeField(u'创建时间', auto_now_add=True)
    extra = models.TextField(u'备注', blank=True, null=True)

    class Meta:
        db_table = u'choir_finances'
        verbose_name = u'财务'
        verbose_name_plural = u'财务'

    def __unicode__(self):
        return self.get_event_display()