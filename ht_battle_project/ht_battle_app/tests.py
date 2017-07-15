# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from mock import patch
from twython import Twython
import helper

class SpellCheckerTestCase(TestCase):

    def test_no_typos(self):
        typos = helper.get_typos('one two three')
        self.assertEqual(typos, 0)

    def test_some_typos(self):
        typos = helper.get_typos('one two three fourq fixve')
        self.assertEqual(typos, 2)


class TwitterTestCase(TestCase):

    def fake_search(self, q, since_id, count):
        return {
            'statuses': ['tweet 1', 'tweet 2']
        }

    @patch.object(Twython, 'search', fake_search)
    def test_get_tweets(self):
        tweets = helper.get_tweets('#test', '12345')
        self.assertEqual(tweets, ['tweet 1', 'tweet 2'])


class RunBattleTestCase(TestCase):

    def fake_get_tweets_no_typos(tag, last_tweet_id):
        return [{
            'id_str': '12345',
            'text': 'one two three'
        }]

    @patch.object(helper, 'get_tweets', fake_get_tweets_no_typos)
    def test_get_tweets_no_typos(self):
        (last_tweet_id, number_of_typos) = helper.run_battle(
            '#test', '12345')
        self.assertEqual((last_tweet_id, number_of_typos), (
            u'12345', 0))

    def fake_get_tweets_typos(tag, last_tweet_id):
        return [{
            'id_str': '12345',
            'text': 'one two thXreXe'
        }]

    @patch.object(helper, 'get_tweets', fake_get_tweets_typos)
    def test_get_tweets(self):
        (last_tweet_id, number_of_typos) = helper.run_battle(
            '#test', '12345')
        self.assertEqual((last_tweet_id, number_of_typos), (
            u'12345', 1))