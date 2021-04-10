import hmac
import hashlib
import requests
import time

class Request(object):
    """ Resembles an abstract API-call """

    def __init__(self, api):
        self.api = api
        self.address = api.address
        self.headers = None
        self.data = {}
        self.request = None
        self.response = None

class SignedRequest(Request):
    """ Resembles an abstract signed API-call """

    def __init__(self, api):
        super().__init__(api)

    def sign(self):
        request = requests.Request('POST', self.address, data=self.data, headers=self.api.headers).prepare()
        signature = hmac.new(self.api.secret.encode('utf-8'), request.body.encode('utf-8'), hashlib.sha256).hexdigest() # TODO: Faster Implementation available sha256()
        self.data['signature'] = signature
        self.request = requests.Request('POST', self.address, data=self.data, headers=self.api.headers)

class Info(Request):
     """ Resembles a GET-API-Call to get exchange info """
     
     def __init__(self, api):
        super().__init__(api)
        self.address += "/exchangeInfo"
        self.response = requests.get(self.address)
        self.request = self.response.request

class Order(Request):
    """ Resembles a POST-API-Call to order assets """

    def __init__(self, api, symbol, quantity, price):
        super().__init__(api)
        self.address += "/order"
        self.data['symbol'] = symbol
        self.data['side'] = "BUY"
        self.data['type'] = "LIMIT"
        self.data['timeInForce'] = "GTC"
        self.data['quantity'] = quantity
        self.data['price'] = price
        self.data['recvWindow'] = 5000
        self.data['timestamp'] = round(time.time()*1000)
        self.sign()
        with requests.Session() as session:
            request = session.prepare_request(self.request)
            self.response = session.send(request)
