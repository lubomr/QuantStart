import json
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing

accountID = "101-004-9226142-001"
access_token="f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0"
api = API(access_token=access_token)
params ={
        "instruments": "EUR_USD"
        }
R = pricing.PricingStream(accountID=accountID, params=params)
rv = api.request(R)
maxrecs = 10


for ticks in iter(rv):

    print(json.dumps(ticks, indent=4),",")
    if maxrecs == 0:
        rv.terminate("maxrecs records received")
