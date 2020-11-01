from bitmex_websocket import BitMEXWebsocket
import time
import bitmex
import config
import json




def buySignal():

      client = bitmex.bitmex(test=True, api_key=config.BMEX_API_ID,
                       api_secret=config.BMEX_API_SECRET)
      print("client started for buying")
      
      ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD",
                     api_key=config.BMEX_API_ID, api_secret=config.BMEX_API_SECRET)
      print ("client connected")
      client.Order.Order_new(symbol='XBTUSD', orderQty=10).result()


def sellSignal():

      client = bitmex.bitmex(test=True, api_key=config.BMEX_API_ID, api_secret=config.BMEX_API_SECRET)
      print("client started for selling")
      
      ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD", api_key=config.BMEX_API_ID, 
                        api_secret=config.BMEX_API_SECRET)
      print("client connected")

      client.Order.Order_new(symbol = 'XBTUSD', orderQty = -10).result()



def run():

      buySignal()


      sellSignal()

      return client

'''
      while(ws.ws.sock.connected): #while connection to bitmex is active
            markPrice = ws.get_instrument()["markPrice"] #getting the mark price
            print('markPrice: ' , markPrice)
            print ('websocket running')           

            if(markPrice < 9700 and markPrice > 9600):
                  print ('marketbuy 250')
                  print ('test order for bmex adapter')
                  #client.Order.Order_new(symbol='XBTUSD', orderQty=250).result() #put in market buy for 100 contracts
                  sleeptime = 3 #modify request interval to 3 seconds
            if(markPrice < 9600 and markPrice > 9500):
                  print ('market buy 500')
                  print ('test order for bmex adapter')
                  #client.Order.Order_new(symbol='XBTUSD', orderQty=500).result()
                  sleeptime = 2
            if(markPrice > 9500):
                  print ('buying 500')
                  print ('test order for bmex adapter')
                  #client.Order.Order_new(symbol='XBTUSD', orderQty=500).result()
                  sleeptime = 1

            time.sleep(sleeptime)
'''

if __name__ == "__main__":
      run()
