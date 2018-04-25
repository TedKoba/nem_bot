from __future__ import absolute_import, unicode_literals
from nem_bot.celery import app
from bot.xem_bot import tweet_nem_price


@app.task
def scheduled_nem_bot():
    tweet_nem_price()
