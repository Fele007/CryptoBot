import broker_api
from request import *

if __name__ == "__main__":
    api = broker_api.Binance()
    #buy_request = Order(api, "BTCBUSD", 0.001, 60000)
    info_request = Info(api)