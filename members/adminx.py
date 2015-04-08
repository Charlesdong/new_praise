# -*- coding: utf-8 -*-
from xadmin import site
from members.models import ChoirMembers


class ChoirMembersAdmin(object):
    list_display = ('name', 'gender', 'native_place', 'join_time', 'baptize_time', 'telephone', 'qq',  'extra')
    search_fields = ['name', 'telephone']

    def join_time(self, obj):
        if obj.join_time:
            print obj.join_time
            return obj.join_time.strftime('%Y-%m-%d')
        return ''

    def baptize_time(self, obj):
        if obj.baptize_time:
            return obj.baptize_time.strftime('%Y-%m-%d')
        return ''



site.register(ChoirMembers, ChoirMembersAdmin)
