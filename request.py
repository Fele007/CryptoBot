import hmac
import hashlib
import requests
import time

def current_milli_time():
    return round(time.time() * 1000)

class Request(object):
    """ Resembles an abstract API-Call """

    def __init__(self, api):
        """ Initializes an API-Call """

        self.api = api
        self.address = api.address
        self.headers = None
        self.data = {}

class Lookup(Request):
    # TODO: Implement
    pass

class Order(Request):
    """ Resembles a POST-API-Call to order assets """

    def __init__(self, api, symbol, quantity, price):
        super().__init__(api)
        self.address += "/v3/order"
        self.data['symbol'] = symbol
        self.data['side'] = "BUY"
        self.data['type'] = "LIMIT"
        self.data['timeInForce'] = "GTC"
        self.data['quantity'] = quantity
        self.data['price'] = price
        self.data['recvWindow'] = 5000
        self.data['timestamp'] = round(time.time()*1000)
        # Prepare request and sign it
        request = requests.Request('POST', self.address, data=self.data, headers=self.api.headers).prepare()
        signature = hmac.new(self.api.secret.encode('utf-8'), request.body.encode('utf-8'), hashlib.sha256).hexdigest() # TODO: Faster Implementation available sha256()
        self.data['signature'] = signature
        request = requests.Request('POST', self.address, data=self.data, headers=self.api.headers).prepare()

        with requests.Session() as session:
            print(request.headers, request.body)
            response = session.send(request)
            print(response)
            print(response.text)