import requests
import json
from event import TickEvent
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing



class StreamingForexPrices(object):
    def __init__(
        self, domain, access_token,
        account_id, instruments, events_queue
    ):
        self.domain = domain
        self.access_token = access_token
        self.account_id = account_id
        self.instruments = instruments
        self.events_queue = events_queue
        self.cur_bid = None
        self.cur_ask = None

    def connect_to_stream(self):
        accountID = "101-004-9226142-001"
        access_token = "f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0"
        api = API(access_token=access_token)
        params = {
            "instruments": "EUR_USD"
        }
        R = pricing.PricingStream(accountID=accountID, params=params)
        rv = api.request(R)
        maxrecs = 10
        return rv


    def stream_to_queue(self):
        response = self.connect_to_stream()
        #if response.status_code != 200:
        #    return
        for line in iter(response):
            print(str(line))
            if "instrument" in line.keys() or "tick" in line.keys():
                print(line)
                instrument = line["instrument"]
                time = line["time"]
                bid = line["bids"]
                ask = line["asks"]

                tev = TickEvent(instrument, time, bid, ask)
                self.events_queue.put(tev)
