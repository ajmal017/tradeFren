from bitmex_websocket import BitMEXWebsocket
import time
import bitmex
import config
import json
import pprint
import datetime

def get_logger():
    '''
    '''

    f = open("logfile.txt", "a")


    client = bitmex.bitmex(test=False, api_key=config.BMEX_API_ID,
                    api_secret=config.BMEX_API_SECRET)
    
    price = client.Quote.Quote_get(symbol='XBTUSD').result()
    #print (price)
    #print (price[0][0])

    ws = BitMEXWebsocket(endpoint="https://www.bitmex.com/api/v1", symbol="XBTUSD",api_key=config.BMEX_API_ID, api_secret=config.BMEX_API_SECRET)
    print ("client started")

    startTime = datetime.datetime.now()

    hours_added = datetime.timedelta(hours=1)
    endTime = startTime + hours_added

    #print (startTime , " , , ," , future_date_and_time)


    while(ws.ws.sock.connected):

        currentTime = datetime.datetime.now()
        if endTime < currentTime:
            get_logger()

        data = ws.get_instrument() #getting the mark price

        depth = ws.get_ticker()
        #print (data)


        dataToLog = str('last Price: ' + str(data['lastPrice']) + 'mark price: ' + str(data['markPrice']) + 'timestamp: ' + str(data['timestamp']) + '\n')

        with open('logfile.txt', 'a') as file:
            file.write(str(dataToLog))



        time.sleep(1)
    


if __name__ == "__main__":
    get_logger()

