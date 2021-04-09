import broker_api, request
from request import Request, Order

if __name__ == "__main__":
    api = broker_api.Binance()
    buy_request = Order(api, "BTCEUR", 1, 40000)