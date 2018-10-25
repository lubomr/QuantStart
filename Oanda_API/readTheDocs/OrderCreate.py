import oandapyV20
import oandapyV20.endpoints.orders as orders
import json

#Create sell limit order at 1.2 with SL 1.22
data = {
        "order": {
                    "price": "1.2",
                    "stopLossOnFill": {
                    "timeInForce": "GTC",
                    "price": "1.22"
                    },
        "timeInForce": "GTC",
        "instrument": "EUR_USD",
        "units": "100",
        "type": "LIMIT",
        "positionFill": "DEFAULT"
        }
    }

accountID = "101-004-9226142-001"
access_token="f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0"
client = oandapyV20.API(access_token="f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0")
r = orders.OrderCreate(accountID, data=data)
client.request(r)
print(r.response)
print(json.dumps(r.response, indent=4))