# -*- coding: utf-8 -*-
from xadmin import site
from activity.models import Priest, Songs, CompereWeekly


class PriestAdmin(object):
    list_display = ('name', 'telephone', 'email', 'extra', )


class SongsAdmin(object):
    list_display = ('name', 'author', 'musicbook', 'mp3', )


class CompereWeeklyAdmin(object):
    list_display = ('compers', 'compe_songs', 'compe_date', 'speaker', 'verse', )


site.register(Priest, PriestAdmin)
site.register(Songs, SongsAdmin)
site.register(CompereWeekly, CompereWeeklyAdmin)

