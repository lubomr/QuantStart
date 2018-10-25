import oandapyV20
import oandapyV20.endpoints.instruments as instruments

client = oandapyV20.API(access_token="f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0")
params = None
r = instruments.InstrumentsOrderBook(instrument="EUR_USD")
client.request(r)
print(r.response)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

