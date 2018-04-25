from django.db import models
from bot.update_status import tweet
from bot.zaif_api import (
    zaif_last_price,
    zaif_ticker,
)

class Price(models.Model):
    time = models.DateTimeField(auto_now=True, db_index=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=4, db_index=True, default=0.0)
    high_price = models.DecimalField(max_digits=10, decimal_places=4, db_index=True, default=0.0)
    low_price = models.DecimalField(max_digits=10, decimal_places=4, db_index=True, default=0.0)
    vwap_price = models.DecimalField(max_digits=10, decimal_places=4, db_index=True, default=0.0)

    class Meta:
        ordering = ['time']
