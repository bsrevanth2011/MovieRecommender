# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserInfo, Movie, Rating

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Movie)
admin.site.register(Rating)