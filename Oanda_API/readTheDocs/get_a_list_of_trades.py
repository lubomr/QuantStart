# get a list of trades
import json
from oandapyV20 import API
import oandapyV20.endpoints.trades as trades

api = API(access_token="f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0")
accountID = "101-004-9226142-001"
r = trades.TradesList(accountID)
# show the endpoint as it is constructed for this call
print("REQUEST:{}".format(r))
rv = api.request(r)
print("RESPONSE:\n{}".format(json.dumps(rv, indent=2)))