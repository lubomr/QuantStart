import requests
import json

from event import TickEvent
instrument = "EUR_USD"
s = requests.Session()
url = "https://stream-fxpractice.oanda.com/v1/prices?instrument=EUR_USD"
# "https://" + self.domain + "/v1/prices"
print(url)
headers = {'Authorization': 'Bearer ' + 'f7e9e4ce6d3053fd67480df1fb51e665-a52e75b6119ff67521f77ebfde0aafe0'}
print("######################################")
print("headers = ",headers)
params = {'instruments': instrument, 'accountId': 'Lubo8810'}
print("params = ",params,"\n")
req = requests.Request('GET', url, headers=headers, params=params)
print("req = ", req)
pre = req.prepare()
print("pre = ", pre)
resp = s.send(requests.Request('GET',url,headers=headers,params=params).prepare(), stream=True, verify=False)
print("######################################")
print("resp = ",resp)

'''



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

    def connect_to_stream(self):
        try:
            s = requests.Session()
            url = "https://api-fxtrade.oanda.com/v1/prices?instruments=EUR_USD"
                #"https://" + self.domain + "/v1/prices"
            print(url)
            headers = {'Authorization' : 'Bearer ' + self.access_token}
            params = {'instruments' : self.instruments, 'accountId' : self.account_id}
            req = requests.Request('GET', url, headers=headers, params=params)
            pre = req.prepare()
            resp = s.send(pre, stream=True, verify=False)
            return resp
        except Exception as e:
            s.close()
            print("Caught exception when connecting to stream\n" + str(e))

    def stream_to_queue(self):
        response = self.connect_to_stream()
        if response.status_code != 200:
            return
        for line in response.iter_lines(1):
            if line:
                try:
                    msg = json.loads(line)
                except Exception as e:
                    print("Caught exception when converting message into json\n" + str(e))
                    return
                if msg.has_key("instrument") or msg.has_key("tick"):
                    print(msg)
                    instrument = msg["tick"]["instrument"]
                    time = msg["tick"]["time"]
                    bid = msg["tick"]["bid"]
                    ask = msg["tick"]["ask"]
                    tev = TickEvent(instrument, time, bid, ask)
                    self.events_queue.put(tev)
'''