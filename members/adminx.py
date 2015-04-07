# -*- coding: utf-8 -*-
from xadmin import site
from members.models import ChoirMembers


class ChoirMembersAdmin(object):
    list_display = ('name', 'gender', 'native_place', 'join_time', 'baptize_time', 'telephone', 'qq',  'extra')

site.register(ChoirMembers, ChoirMembersAdmin)
