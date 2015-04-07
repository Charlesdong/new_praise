# -*- coding: utf-8 -*-
from xadmin import site
from sign.models import ChoirSign


class ChoirSignAdmin(object):
    list_display = ('name', 'sign_date', )


site.register(ChoirSign, ChoirSignAdmin)
