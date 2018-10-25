import oandapyV20
import oandapyV20.endpoints.orders as orders

#cancel pending order.

accountID = "101-004-9226142-001"
access_token="f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0"
client = oandapyV20.API(access_token=access_token)
r = orders.OrderCancel(accountID= accountID, orderID=117)
client.request(r)
print(r.response)
