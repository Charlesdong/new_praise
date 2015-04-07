# -*- coding: utf-8 -*-
from xadmin import site
from finance.models import ChoirFinances


class ChoirFinancesAdmin(object):
    list_display = ('member', 'money', 'operation', 'is_devote', 'sum', 'devote_time', 'extra')


site.register(ChoirFinances, ChoirFinancesAdmin)



