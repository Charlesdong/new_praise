# -*- coding: utf-8 -*-
from xadmin import site
from sign.forms import ChoirSignAdminForm
from sign.models import ChoirSign


class ChoirSignAdmin(object):
    list_display = ('member', 'sign_date', )
    form = ChoirSignAdminForm
    list_filter = ('sign_date', )
    search_fields = ['member__name']


site.register(ChoirSign, ChoirSignAdmin)
