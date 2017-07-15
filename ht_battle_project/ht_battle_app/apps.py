# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig
import os
import threading
import time
from helper import check_twitter

def heartbeat():
    while True:
        time.sleep(10)
        check_twitter()

class HtBattleAppConfig(AppConfig):
    """ Using the 'ready' handle that Django provides """
    name = 'ht_battle_app'

    def ready(self):
        """ Executed twice by Django, must check RUN_MAIN to
        avoid running two threads """
        if os.environ.get('RUN_MAIN') is not None:
            pass
            #single_thread = threading.Thread(
            #    target=heartbeat, name='twitter_checker')
            #single_thread.start()


