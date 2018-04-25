import json
import requests

class zaif_last_price:
    def __init__(self, currency_pair):
        self.url = 'https://api.zaif.jp/api/1/last_price/'+currency_pair
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception('return status code is {}'.format(response.status_code))
        self.response = json.loads(response.text)

    def get_price(self):
        return self.response['last_price']


'''
{
    "last": 135875.0,
    "high": 136000.0,
    "low": 131570.0,
    "vwap": 133301.7489,
    "volume": 6889.215,
    "bid": 135875.0,
    "ask": 135920.0
}
キー	詳細	型
last	終値	float
high	過去24時間の高値	float
low	過去24時間の安値	float
vwap	過去24時間の加重平均	float
volume	過去24時間の出来高	float
bid	買気配値	float
ask	売気配値	float
補足
'''
class zaif_ticker:
    def __init__(self, currency_pair):
        self.url = 'https://api.zaif.jp/api/1/ticker/'+currency_pair
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception('return status code is {}'.format(response.status_code))
        self.response = json.loads(response.text)

    def get_last(self):
        return self.response['last']

    def get_high(self):
        return self.response['high']

    def get_low(self):
        return self.response['low']

    def get_vwap(self):
        return self.response['vwap']

    def get_volume(self):
        return self.response['volume']

    def get_bid(self):
        return self.response['bid']

    def get_ask(self):
        return self.response['ask']
