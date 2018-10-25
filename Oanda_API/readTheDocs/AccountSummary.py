import oandapyV20
import oandapyV20.endpoints.accounts as accounts
import json

#api = API(access_token="f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0")
accountID = "101-004-9226142-001"
client = oandapyV20.API(access_token="f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0")
r = accounts.AccountSummary(accountID)
client.request(r)
print(r.response)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(r.response['account'])
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for x in r.response:
    print(x)
    print("{")
    for y in r.response[x]:
        if hasattr(y,'__iter__'):
            print("    ",y,':',r.response[x][y])
        else:print(r.response[x])
    print("}")