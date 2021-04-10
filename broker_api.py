import os
from OpenSSL.crypto import sign

class Binance(object):
    """ Encapsules communication with Binance """

    def __init__(self):
        """ Initialize bot and API """

        try:
            self.key=os.environ["crypto_bot_api_key"]
            self.secret=os.environ["crypto_bot_secret_key"]
        except:
            print("No API-key information available")

        self.address = "https://testnet.binance.vision/api/v3"
        self.headers={"X-MBX-APIKEY": self.key}






        # TODO: Was ist das --> wss://testnet.binance.vision/ws     
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
        # TODO: Was ist das --> wss://testnet.binance.vision/stream    

