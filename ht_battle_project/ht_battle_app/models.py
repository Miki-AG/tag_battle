""" This module describes the Battle model """

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Battle(models.Model):
    """ Tag Battle model """
    tag_1 = models.CharField(max_length=140)
    tag_2 = models.CharField(max_length=140)
    tag_1_last_tweet_id = models.CharField(
        max_length=100, null=True, blank=True)
    tag_2_last_tweet_id = models.CharField(
        max_length=100, null=True, blank=True)
    tag_1_typos = models.IntegerField(null=True, blank=True, default=0)
    tag_2_typos = models.IntegerField(null=True, blank=True, default=0)

    start = models.DateTimeField('Start of the battle')
    end = models.DateTimeField('End of the battle')

    def __unicode__(self):
        return ('[{:11}] '
                '\t{} ({}) vs {} ({})').format(
                    self.status(),
                    self.tag_1, self.tag_1_typos,
                    self.tag_2, self.tag_2_typos)

    def is_active(self):
        """ Battle is active

        Returns:
            True if battle is active.
        """
        return (self.start < timezone.now()
                and self.end > timezone.now())

    def has_finished(self):
        """ Battle has finished

        Returns:
            True if battle has finished.
        """
        return self.end > timezone.now()

    def status(self):
        """ Returns text status

        Returns:
            Current status of the battle.
        """
        if self.is_active():
            return 'RUNNING'
        elif self.start > timezone.now():
            return 'NOT STARTED'
        else:
            return 'FINISHED'
