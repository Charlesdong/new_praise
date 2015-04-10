# -*- coding: utf-8 -*-
from xadmin import site
from finance.forms import CompereWeeklyAdminForm
from finance.models import ChoirFinances, TotalMoney


class TotalMoneyAdmin(object):
    list_display = ('total_money', 'createtime')


class ChoirFinancesAdmin(object):
    list_display = ('devote_time', 'money', 'operation', 'extra')
    form = CompereWeeklyAdminForm


site.register(ChoirFinances, ChoirFinancesAdmin)
site.register(TotalMoney, TotalMoneyAdmin)



