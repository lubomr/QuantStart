import oandapyV20
import oandapyV20.endpoints.instruments as instruments
client = oandapyV20.API(access_token="f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0")

#Set parameters for last 10 Day candles.
params={"count":10,"granularity":"D"}

r = instruments.InstrumentsCandles(instrument="EUR_USD",params=params)
client.request(r)
print(r.response)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
for x in r.response.items():
    if not isinstance(x[1],list):
        print(x)
    else: print(x[0])
    for y in x:
        if isinstance(y,list):
            for i in y:
                print(i)