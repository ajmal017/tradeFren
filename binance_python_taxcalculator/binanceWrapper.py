from binance.client import Client
from datetime import datetime
import time
import os
import json
import pprint 

def give_time(k):
    '''
    helper method to make time format out of binance unique timestamp

        args:
            k : a binance formatted timestamp
        return: a datetime string
    ''' 
    return str(datetime.fromtimestamp(int(k)/1000))

def get_trade_history(userForm):
    '''
    collects the trade history of a given user and uploads it to
    the mongodb instance

        args:
            userForm: a json file containing authentication data
                {'_id': ObjectId(''), 'api_key': '', 'api_secret': '', 'username': ''}
        
        return:
            symbols : a dictionary with trade pairs in json format
            symbol_list : a list with the actively traded tickers 
    '''
    
    # initialize client
    API_KEY = userForm['api_key']
    API_SECRET = userForm['api_secret']
    client = Client(API_KEY, API_SECRET)
    #time_res = client.get_server_time()
    #time = time_res['serverTime']
    
    info = client.get_exchange_info() #get exchange info
    
    symbol_list = list() #creating a list for storage of all existing trade pairs
    trade_history = list() #list for storing trade history
    account_balance = list() #list for storing account balance
    symbols = {} #dictionary of trade pairs with trade history

    for i in info.get('symbols'):  # loop through all existing trade pairs
        symbol_list.append(i['symbol'])  # add each trade pair
    


    count = 0

    symbol_final = list()

    for i in symbol_list: #for each symbol
        tmp = client.get_my_trades(symbol=i, startTime=1546300800000)
        if tmp != []:
            symbols[i] = tmp
            symbol_final.append(i)
        if count == 3:
            break
        count += 1

    user_symbols = {
        'username': userForm['username'],
        'symbols': symbol_final
    }
    
    return symbols, user_symbols

    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint (symbols.get('BNBBTC'))
