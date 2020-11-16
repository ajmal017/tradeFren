from bitmex_websocket import BitMEXWebsocket
import time
import bitmex
import config
import json
import pprint




def calcPosSize(ws, percentage, leverage):
      '''
      Used to calculate amount of contracts for opening a position
      '''

      data = ws.funds()
      currentPrice = ws.get_instrument()
      askPrice = currentPrice['askPrice']
      orderQty = int(data["walletBalance"])*int(percentage)/1000000000
      contractSize = (float(askPrice) * (float(orderQty) * float(leverage)))


      return contractSize



def buySignal(percentage, leverage):
      '''
      Processes a BUY signal from json file provided by a tradingview webhook.

            data: a json file
            percentage: the percentage of funds to use for trade
      '''

      client = bitmex.bitmex(test=True, api_key=config.BMEX_API_ID,
                       api_secret=config.BMEX_API_SECRET)
      print("client started for buying")
      
      ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD",
                     api_key=config.BMEX_API_ID, api_secret=config.BMEX_API_SECRET)
      print ("client connected")

      '''
      data = ws.funds()
      currentPrice = ws.get_instrument()
      askPrice = currentPrice['askPrice']
      orderQty = int(data["walletBalance"])*int(percentage)/1000000000
      contractSize = (float(askPrice) * (float(orderQty) * float(leverage)))
      '''

      contractSize = calcPosSize(ws, percentage, leverage)

      print ("amount contracts" , contractSize)

      client.Order.Order_new(symbol='XBTUSD', orderQty=contractSize).result()


def sellSignal(data):
      '''
      Processes a SELL signal from json file provided by a tradingview webhook.

            data: a json file
      '''

      client = bitmex.bitmex(test=True, api_key=config.BMEX_API_ID, api_secret=config.BMEX_API_SECRET)
      print("client started for selling")
      
      ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD", api_key=config.BMEX_API_ID, 
                        api_secret=config.BMEX_API_SECRET)
      print("client connected")

      client.Order.Order_new(symbol = 'XBTUSD', orderQty = -10).result()

def get_funds(percentage):
      '''
      sends a request to bitmex requesting the funds of an account

            params:
                  percentage: the percentage of the total funds used for the next trade
      '''

      client = bitmex.bitmex(
            test=True, api_key=config.BMEX_API_ID, api_secret=config.BMEX_API_SECRET)
      ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD", api_key=config.BMEX_API_ID,
                              api_secret=config.BMEX_API_SECRET)


      data = ws.funds()
      currentPrice = ws.get_instrument()
      askPrice = currentPrice['askPrice']
      #print ("///////////xxxx/////////")
      #currentPrice2 = ws.get_ticker()
      #print (currentPrice2)

      print ("askprice" , askPrice)

      '''
      for x, y in data.items():
            print (x, y)
            '''

      orderQty = int(data["walletBalance"])*int(percentage)/1000000000
      
      return data, orderQty, askPrice




      

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
      get_funds()
