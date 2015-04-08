# -*- coding: utf-8 -*-
from django.db import models
from members.models import ChoirMembers


class ChoirSign(models.Model):
    member = models.ManyToManyField(ChoirMembers, verbose_name=u'姓名')
    sign_date = models.DateField(u'签到日期')

    class Meta:
        db_table = u'choir_sign'
        verbose_name = u'签到'
        verbose_name_plural = u'签到'

    def __unicode__(self):
        return self.sign_date.strftime("%Y-%m-%D")

