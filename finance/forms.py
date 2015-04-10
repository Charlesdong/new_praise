# -*- coding: utf-8 -*-
from django import forms
from django.forms import HiddenInput
from finance.models import ChoirFinances, TotalMoney


class CompereWeeklyAdminForm(forms.ModelForm):
    total_money = forms.FloatField(widget=HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        super(CompereWeeklyAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ChoirFinances

    def save(self, commit=True):
        instance = forms.ModelForm.save(self, commit)
        obj = TotalMoney.objects.latest('createtime')
        if instance.operation:
            # 收入
            total_money = obj.total_money + instance.money
        else:
            # 支出
            total_money = obj.total_money - instance.money
        total_obj = TotalMoney(total_money=total_money).save()
        instance.total_money = total_obj
        instance.save()
        return instance


