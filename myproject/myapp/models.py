# -*- coding: utf-8 -*-
from django.db import models


class LogFile(models.Model):
    docfile = models.FileField(upload_to='log_file/%Y/%m/%d')
