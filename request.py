import hmac
import hashlib

def item_to_param(item): 
    return "{}={}".format(item[0], item[1])

class Request(object):
    """ Resembles an abstract API-Call """

    def __init__(self, method, target):
        """ Initializes an API-Call """

        self.method = method
        self.target = target
        self.params = {}
        self.query_string = None

    def compose_query_string(self):
        return self.method + " " + self.target + " " + "&".join(map(item_to_param, self.params.items()))

    def sign(self, api):
        signature = hmac.new(api.secret.encode('utf-8'), self.query_string.encode('utf-8'), hashlib.sha256).hexdigest()
        self.params['signature'] = signature
        self.query_string = self.compose_query_string()
        return self.query_string

class Order (Request):
    """ Resembles a POST-API-Call to order assets """

    def __init__(self, symbol, quantity, price):
        super().__init__("POST", "/api/v3/order")
        self.params['symbol'] = symbol
        self.params['side'] = "BUY"
        self.params['type'] = "LIMIT"
        self.params['timeInForce'] = "GTC"
        self.params['quantity'] = quantity
        self.params['price'] = price
        self.params['recvWindow'] = 5000
        self.params['timestamp'] = None       # TODO: Implement Timestamp
        self.query_string = self.compose_query_string()

   
      


