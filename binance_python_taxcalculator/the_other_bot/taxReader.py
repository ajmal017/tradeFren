from binance.client import Client
import config
from datetime import datetime
import time
import helper
import os
import json

client = Client(config.API_ID, config.API_SECRET)

logfile=open("logfile.txt" , "a")
symbols=open("symbollog.txt", "a")
jsonfiles=open("jsonfiles.json", "a")
history=open("jsonhistory.json" , "a")

time_res = client.get_server_time()
print (time_res['serverTime'])
print(helper.give_time(time_res['serverTime']))

info = client.get_exchange_info() # https://python-binance.readthedocs.io/en/latest/binance.html#binance.client.Client.get_exchange_info

symbol_list = list() #creating a list for storage of all existing trade pairs
  
trade_history = list() #list for storing trade history
account_balance = list()#list for storing account balance

counter = 0
menuValg1 = input("Do you wish to import trade symbols again? If you have not imported it they will be imported anyway. Type 'Y' or 'N'")

if menuValg1 == "y" or os.path.getsize('symbollog.txt') == 0:

      for i in info.get('symbols'):  # loop through trade pairs
            symbol_list.append(i['symbol'])  # add each trade pair
            #print('added', i['symbol'])"""  """

      for i in symbol_list: #loop through trade pairs
            tmp = client.get_my_trades(symbol=i, startTime=1556661600000)
            if tmp != []: #if the trade pair has existing trade history
                  # add it to trading history
                  symbols.write(i + "\n")
                  print ('found trade history for ' , i)
                  trade_history.append(tmp)
                  #print ('counter er ' , counter)
      symbols.close()
      with open('logfile.txt', 'w') as filehandle:
            for tradeIter in trade_history:
                  logfile.write('%s\n' % tradeIter)
      logfile.close()

else:
      menuValg2 = input("Do you wish to re-import trades? If trades have not been imported yet trades will be imported. Type y or n: ")
      if menuValg2 == "y" or os.path.getsize('logfile.txt') == 0:
            with open ("symbollog.txt") as symbolIter:
                  for line in symbolIter:
                        tmpjson = open('./json/%s.json' % line.rstrip(), "a")
                        symbol_list.append(line)
                        tmp = client.get_my_trades(symbol=line.strip(), startTime=1556661600000)
                        trade_history.append(tmp)
                        json.dump(tmp, tmpjson, indent=0)
                        json.dump(tmp, jsonfiles, indent=0)
                        tmpjson.close()
                  with open('logfile.txt', 'w') as filehandle:
                        for tradeIter in trade_history:
                              logfile.write('%s\n' % tradeIter)
                  logfile.close()
                  jsonfiles.close()


with open('jsonfiles.json', 'r') as infile:
    data = infile.read()
    new_data = data.replace('][', ',')
    json_data = json.loads(f'[{new_data}]')

for x in sorted(json_data, key=lambda k: k[0].get('time'), reverse=True):
      for i in x:
            json.dump(i, history, indent=0)
history.close()

tradeFees = []

hifo = [] #Highest In First Out
fifo = [] #First In First Uut
lifo = [] #Last In First Out
lofo = [] #LOwest-in First Out

#makes stacks with trades 
with open("symbollog.txt") as symbolIter:
      for line in symbolIter:
            tmpjson = open('./json/%s.json' % line.rstrip(), "r")
            parsed = json.load(tmpjson)
            
            lifo = parsed

            fifo = sorted (parsed,key = helper.sort_help_time, reverse = True)

            hifo = sorted(parsed, key=helper.sort_help_price)

            lofo = sorted(parsed, key=helper.sort_help_price, reverse = True)
            
            break

print ('fifo')
for i in fifo:
      print(helper.give_time(i['time']), ' ', i['price'], ' ', i['isBuyer'])

print ('hifo')
for i in hifo:
      print(helper.give_time(i['time']), ' ', i['price'], ' ', i['isBuyer'])

print('lifo')
for i in lifo:
      print(helper.give_time(i['time']), ' ', i['price'], ' ', i['isBuyer'])

print('lofo')
for i in range(len(lofo)):
     print(helper.give_time(lofo[i]['time']), ' ', lofo[i]['price'], ' ', lofo[i]['isBuyer'])



