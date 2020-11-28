from bitmex_websocket import BitMEXWebsocket
import time
import bitmex
import config
import json
import pprint


def get_logger():
    '''
    rerturn a bitex client also logs blabla this is prob outdated
    '''

    f = open("logfile.txt", "a")


    client = bitmex.bitmex(test=False, api_key=config.BMEX_API_ID,
                       api_secret=config.BMEX_API_SECRET)
    

    price = client.Quote.Quote_get(symbol='XBTUSD').result()
    #print (price)
    #print (price[0][0])

    ws = BitMEXWebsocket(endpoint="https://www.bitmex.com/api/v1", symbol="XBTUSD",api_key=config.BMEX_API_ID, api_secret=config.BMEX_API_SECRET)

    while(ws.ws.sock.connected):
        markPrice = ws.get_instrument() #getting the mark price

        print(markPrice['lastPrice'])

        with open('logfile.txt', 'a') as file:
            file.write(str(markPrice['lastPrice'])+'\n')

        time.sleep(5)
    




   
    return client





if __name__ == "__main__":

    ws = get_logger()
