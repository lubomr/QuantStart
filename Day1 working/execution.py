import http.client
import urllib
import oandapyV20
import oandapyV20.endpoints.orders as orders
import json
from oandapyV20 import API
from oandapyV20.contrib.requests import MarketOrderRequest

class Execution(object):
    def __init__(self, domain, access_token, account_id):
        self.domain = domain
        self.access_token = access_token
        self.account_id = account_id
        self.conn = self.obtain_connection()

    def obtain_connection(self):
        return http.client.HTTPSConnection(self.domain)

    def execute_order(self, event):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Bearer " + self.access_token
        }
        params = urllib.parse.urlencode({
            "instrument" : event.instrument,
            "units" : event.units,
            "type" : event.order_type,
            "side" : event.side
        })
        if event.side=='buy':
            ammount=1000
        else: ammount = -1000

        accountID = "101-004-9226142-001"
        access_token = "f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0"
        client = API(access_token=access_token)
        mo = MarketOrderRequest(instrument="EUR_USD", units=ammount)
        # now we have the order specification, create the order request
        r = orders.OrderCreate(accountID, data=mo.data)
        # perform the request
        rv = client.request(r)
        print(json.dumps(rv, indent=4))
