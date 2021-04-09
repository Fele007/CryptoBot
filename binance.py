class Binance(object):
    """ Encapsules communication with Binance """

    def __init__(self):
        """ Initialize bot and API """

        # Set API-keys
        try:
            apiKey=os.environ["crypto_bot_api_key"]
            apiSecret=os.environ["crypto_bot_secret_key"]
        except:
            print("No API-key information available")

        # Set and test api
        self.address = "https://testnet.binance.vision/api"
        #wss://testnet.binance.vision/ws     Secure Version??
        """ 
        Request:
        GET /chat HTTP/1.1
         Host: server.example.com
         Upgrade: websocket
         Connection: Upgrade
         Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
         Origin: http://example.com
         Sec-WebSocket-Protocol: chat, superchat
         Sec-WebSocket-Version: 13 
         
         Answer:
         HTTP/1.1 101 Switching Protocols
         Upgrade: websocket
         Connection: Upgrade
         Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
         Sec-WebSocket-Protocol: chat
         """
        #wss://testnet.binance.vision/stream

def sign():
    pass