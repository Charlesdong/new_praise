# -*- coding: utf-8 -*-
from django import forms
from xadmin.plugins.multiselect import SelectMultipleTransfer
from activity.models import CompereWeekly, Songs
from members.models import ChoirMembers


class CompereWeeklyAdminForm(forms.ModelForm):
    compers = forms.ModelMultipleChoiceField(queryset=ChoirMembers.objects.all(),
                                             widget=SelectMultipleTransfer('compers', is_stacked=False),
                                             required=False, label=u'主礼人')
    compe_songs = forms.ModelMultipleChoiceField(queryset=Songs.objects.all(),
                                                 widget=SelectMultipleTransfer('compe_songs', is_stacked=False),
                                                 required=False, label=u'本周歌曲')

    def __init__(self, *args, **kwargs):
        super(CompereWeeklyAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CompereWeekly


