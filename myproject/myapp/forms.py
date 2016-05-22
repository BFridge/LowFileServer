# -*- coding: utf-8 -*-

from django import forms


class LogFileForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
