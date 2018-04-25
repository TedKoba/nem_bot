from bot.update_status import tweet
from bot.zaif_api import (
    zaif_last_price,
    zaif_ticker,
)
from bot.models import Price
from bot.get_times import manage_time


def tweet_nem_price():
    latest_record = Price.objects.last()
    current_time = manage_time()
    if (latest_record is not None) and ((latest_record.time.hour - 1) == current_time.get_hour()):
        previous_price = latest_record.current_price
    else:
        previous_price = None

    xem_last_price = zaif_last_price('xem_jpy')
    current_price = xem_last_price.get_price()
    xem_ticker = zaif_ticker('xem_jpy')
    if previous_price == None:
        text = "NEM\n現在の価格: {}\n過去24時間の高値: {}\n過去24時間の安値: {}\n過去24時間の加重平均{}".format(current_price, xem_ticker.get_high(), xem_ticker.get_low(), xem_ticker.get_vwap())
    else:
        percentage = round(
            ((current_price-previous_price)/previous_price)*100,
            2
        )
        text = "NEM\n現在の価格: {}\n1時間前との差: {}%\n過去24時間の高値: {}\n過去24時間の安値: {}\n過去24時間の加重平均{4}".format(current_price, percentage, xem_ticker.get_high(), xem_ticker.get_low(), xem_ticker.get_vwap())

    tweet(text)

    new_record = Price(
        current_price=current_price,
        high_price=xem_ticker.get_high(),
        low_price=xem_ticker.get_low(),
        vwap_price=xem_ticker.get_vwap()
    )
    new_record.save()
