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

def get_client_apidb():
    '''
    estabilishis connection to the mongodb database for user APIs
        
        return: a database object
    '''

    client = MongoClient(
        "mongodb+srv://dpball:" + config.ATLAS_PASS + "@cluster0-1ueai.mongodb.net/test?retryWrites=true&w=majority")
    db = client.apidb

    return db

def get_client_tradelogs():
    '''
    estabilishes connection the the mongodb database for trade logs
    
        return: a database object
    '''

    client = MongoClient(
        "mongodb+srv://dpball:" + config.ATLAS_PASS + "@cluster0-1ueai.mongodb.net/test?retryWrites=true&w=majority")
    db = client.tradelogs

    return db

def make_user(userForm):
    '''
    takes a dictionary and uploads it to the mongoDB atlas instance for the specified exchange

    CURRENTLY ONLY FOR BINANCE

        args:
            userForm : a dictionary containing:
                'api_key'
                'api_secret'
                'username'
    '''

    db = get_client_apidb()
    db.binanceUsers.insert_one(userForm)


def retrieve_symbols(username):
    '''
    returns the trade logs for a user

        args:
            username : the username in the apidb database
        return:
            symbols : a list of the users tickers
    '''
    
    db = get_client_apidb()
    userSymbols = db.usersymbols.find_one({"username": username})

    return userSymbols['symbols']


def get_trade_log_binance(username):
    '''
    connects to binance and collects the trade log from given user
    creates a corresponding database for trade logs in a database with users username

        args:
            username : the username of the user we collects the trade log from
    '''
    db = get_client_tradelogs()
    dbUser = get_client_apidb()
    userData = dbUser.binanceUsers.find_one({"username": username})
    tradeHistory, symbol_list = bw.get_trade_history(userData)

    print (symbol_list)

    db[username].insert_one(tradeHistory) # inserts the trade log into tradelogs/username collection
    dbUser.usersymbols.insert_one(symbol_list) # inserts the traded symbols to apidb/usersymbols

if __name__ == "__main__":
    '''
    contains the test mothods for now
    '''

    #get_trade_log_binance('taxbot')
    retrieve_symbols('taxbot')

    #test for maker_user(userForm)
    #data = {
    #"api_key": "123",
    #"api_secret": "345",
    #"username": "testUser1"
    #}
    #make_user(data)

    # next test
