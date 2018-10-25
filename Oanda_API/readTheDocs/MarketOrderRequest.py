import json
from oandapyV20 import API
import oandapyV20.endpoints.orders as orders
from oandapyV20.contrib.requests import MarketOrderRequest

accountID = "101-004-9226142-001"
access_token="f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0"
client = API(access_token=access_token)
mo = MarketOrderRequest(instrument="EUR_USD", units=-10000)
print(json.dumps(mo.data, indent=4))

'''
                                                                {
                                                                    "order": {
                                                                        "type": "MARKET",
                                                                        "positionFill": "DEFAULT",
                                                                        "instrument": "EUR_USD",
                                                                        "timeInForce": "FOK",
                                                                        "units": "10000"
                                                                    }
                                                                }
                                                                '''
# now we have the order specification, create the order request
r = orders.OrderCreate(accountID, data=mo.data)
# perform the request
rv = client.request(r)
#print(rv)
print(json.dumps(rv, indent=4))
'''
    {
        "orderFillTransaction": {
            "reason": "MARKET_ORDER",
            "pl": "0.0000",
            "accountBalance": "97864.8813",
            "units": "10000",
            "instrument": "EUR_USD",
            "accountID": "101-004-1435156-001",
            "time": "2016-11-11T19:59:43.253587917Z",
            "type": "ORDER_FILL",
            "id": "2504",
            "financing": "0.0000",
            "tradeOpened": {
                "tradeID": "2504",
                "units": "10000"
            },
            "orderID": "2503",
            "userID": 1435156,
            "batchID": "2503",
            "price": "1.08463"
        },
        "lastTransactionID": "2504",
        "relatedTransactionIDs": [
            "2503",
            "2504"
        ],
        "orderCreateTransaction": {
            "type": "MARKET_ORDER",
            "reason": "CLIENT_ORDER",
            "id": "2503",
            "timeInForce": "FOK",
            "units": "10000",
            "time": "2016-11-11T19:59:43.253587917Z",
            "positionFill": "DEFAULT",
            "accountID": "101-004-1435156-001",
            "instrument": "EUR_USD",
            "batchID": "2503",
            "userID": 1435156
        }'''