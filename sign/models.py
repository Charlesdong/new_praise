# -*- coding: utf-8 -*-
from django.db import models
from members.models import ChoirMembers


class ChoirSign(models.Model):
    name = models.ForeignKey(ChoirMembers)
    sign_date = models.DateField(u'签到日期', auto_now_add=True)

    class Meta:
        db_table = u'choir_sign'

    def __unicode__(self):
        return self.sign_date

