# -*- coding: utf-8 -*-
from django import forms
from xadmin.plugins.multiselect import SelectMultipleTransfer
from members.models import ChoirMembers
from sign.models import ChoirSign


class ChoirSignAdminForm(forms.ModelForm):
    member = forms.ModelMultipleChoiceField(queryset=ChoirMembers.objects.all(),
                                            widget=SelectMultipleTransfer('member', is_stacked=False),
                                            required=False, label=u'诗班成员')

    def __init__(self, *args, **kwargs):
        super(ChoirSignAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ChoirSign


