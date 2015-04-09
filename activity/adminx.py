# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from activity.forms import CompereWeeklyAdminForm
from activity.models import Priest, Songs, CompereWeekly
from finance.models import ChoirFinances
from members.models import ChoirMembers
from sign.models import ChoirSign


class GlobalSetting(object):
    global_models_icon = {
        Songs: 'fa fa-try',
        Priest: 'fa fa-vimeo-square',
        CompereWeekly: 'fa fa-map-marker',
        ChoirSign: 'fa fa-bookmark',
        ChoirMembers: 'fa fa-camera',
        ChoirFinances: 'fa fa-instagram',
    }
    apps_label_title = {
        'sign': u'考勤管理',
        'finance': u'财务管理',
        'members': u'诗班成员管理',
        'activity': u'上台管理',
        'auth': u'管理员'
    }
    site_title = u'新的赞美管理后台'
    menu_style = 'accordion'
xadmin.site.register(views.CommAdminView, GlobalSetting)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)


class PriestAdmin(object):
    list_display = ('name', 'telephone', 'email', 'extra', )
    search_fields = ['name']


class SongsAdmin(object):
    list_display = ('name', 'author', 'musicbook', 'mp3', )
    search_fields = ['name']


class CompereWeeklyAdmin(object):
    list_display = ('compers', 'compe_songs', 'compe_date', 'speaker', 'verse', )
    search_fields = ['compers__name', 'compe_songs__name']
    list_filter = ('compe_date', )
    form = CompereWeeklyAdminForm


xadmin.site.register(Priest, PriestAdmin)
xadmin.site.register(Songs, SongsAdmin)
xadmin.site.register(CompereWeekly, CompereWeeklyAdmin)

