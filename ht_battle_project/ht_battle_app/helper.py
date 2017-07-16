# -*- coding: utf-8 -*-
""" Helper functions """
from django.core.exceptions import AppRegistryNotReady
from django.conf import settings
from enchant.checker import SpellChecker
from twython import Twython

def check_twitter():
    """ Periodically check for active battles """
    try:
        from models import Battle
        for battle in Battle.objects.all():
            print '\nBattle: {} vs {}\n'.format(
                battle.tag_1, battle.tag_2)
            typos_1 = 0
            typos_2 = 0
            if battle.is_active():
                (battle.tag_1_last_tweet_id,
                 typos_1) = run_battle(
                     battle.tag_1, battle.tag_1_last_tweet_id)
                (battle.tag_2_last_tweet_id,
                 typos_2) = run_battle(
                     battle.tag_2, battle.tag_2_last_tweet_id)
                battle.tag_1_typos += typos_1
                battle.tag_2_typos += typos_2
            battle.save()
    except AppRegistryNotReady:
        pass

def run_battle(tag, last_tweet_id):
    """ Get tweets and calculate typos for a given tag.

    Args:
        tag: The tag to be processed.
        last_tweet_id: Id of he last tweet retrieved.

    Returns:
        Tuple containing the last tweet id and number of typos.
    """
    tweets = get_tweets(tag, last_tweet_id)
    is_first = True
    number_of_typos = 0
    for tweet in tweets:
        if is_first:
            last_tweet_id = tweet['id_str']
            is_first = False
        number_of_typos += get_typos(tweet['text'].encode('utf-8'))
    return (last_tweet_id, number_of_typos)

def get_tweets(tag, since_id):
    """ Get tweets

    Args:
        tag: The tag to be processed.
        since_id: Id of he last tweet retrieved.

    Returns:
        All tweets for that specific tag.
    """
    twitter = Twython(
        app_key=settings.TWITTER_APP_KEY,
        app_secret=settings.TWITTER_APP_KEY_SECRET,
        oauth_token=settings.TWITTER_ACCESS_TOKEN,
        oauth_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)
    search = twitter.search(q=tag, since_id=since_id, count=5)
    return search['statuses']

def get_typos(text):
    """ Get typos (words not correct according to an en_US
        spell checker)

    Args:
        text: Text to be processed.

    Returns:
        Number of typos for that text.
    """
    spell_checker = SpellChecker("en_US")
    spell_checker.set_text(text)
    print '\n\tTweet: {}'.format(text)
    typos = [typo.word for typo in spell_checker]
    print '\tTypos: {} {}'.format(len(typos), typos)
    return len(typos)
