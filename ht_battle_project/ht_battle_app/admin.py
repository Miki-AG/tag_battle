# -*- coding: utf-8 -*-

""" Configuration of the admin models """
from __future__ import unicode_literals

from django.contrib import admin
from ht_battle_app.models import Battle


class BattleAdmin(admin.ModelAdmin):
    """ Models in Admin registerd here"""
    fields = [
        'tag_1', 'tag_2',
        'tag_1_typos', 'tag_2_typos',
        'start', 'end']
    readonly_fields = ['tag_1_typos', 'tag_2_typos']

admin.site.register(Battle, BattleAdmin)
