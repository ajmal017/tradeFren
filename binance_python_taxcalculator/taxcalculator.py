import re
import json
import os
from pymongo import MongoClient
import dns
import pymongo
import ssl
import config
import pprint
import binanceWrapper as bw
from binance.client import Client
from datetime import datetime
import time
import test.test_script_helper
import helper
import pprint
from bson.son import SON


def sort_help_price(d):
      return d['price']


def get_tradelog(username):
    '''
    Retrieves the tradelog from mongodb instance from the given user
        
        args:
            username : the trade log to retreieve 
    '''
    db = helper.get_client_tradelogs()
    tradeCollection = db[username]
    tradeList = tradeCollection.find({},{'_id' : 0})

    theList = list(tradeList)

    symbolIter = helper.retrieve_symbols(username)

    for i in symbolIter:
        test = theList[0].get('ETHBTC')
        test = sorted(test, key=lambda k: k['price'], reverse=False) 
    


    #pprint.pprint (test)


if __name__ == "__main__":
    '''
    contains the test mothods for now
    '''

    get_tradelog("taxbot")