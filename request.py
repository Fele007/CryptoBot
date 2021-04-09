import hmac
import hashlib
import requests

class Request(object):
    """ Resembles an abstract API-Call """

    def __init__(self, api):
        """ Initializes an API-Call """

        self.api = api
        self.headers = None
        self.data = {}


class Order (Request):
    """ Resembles a POST-API-Call to order assets """

    def __init__(self, api, symbol, quantity, price):
        super().__init__(api)
        self.data['symbol'] = symbol
        self.data['side'] = "BUY"
        self.data['type'] = "LIMIT"
        self.data['timeInForce'] = "GTC"
        self.data['quantity'] = quantity
        self.data['price'] = price
        self.data['recvWindow'] = 5000
        self.data['timestamp'] = None       # TODO: Implement Timestamp
        # Prepare request and sign it
        request = requests.Request('POST', self.api.address, data=self.data, headers=self.api.headers).prepare()
        signature = hmac.new(self.api.secret.encode('utf-8'), request.body.encode('utf-8'), hashlib.sha256).hexdigest() # TODO: Faster Implementation available sha256()
        request.headers['Sign'] = signature


    #   with requests.Session() as session:
    #        response = session.send(prepped)