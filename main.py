from flask import Flask, request, Response
from pyngrok import ngrok
import json
import tradingview_adapter as tview
import bitmex_adapter as bmex
import argparse
from flask import Flask
from flask import render_template
from flask import request
import sys
import os


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':

        if(data["action"] == "buy" or data["action"] == "strongbuy"):
            bmex.buySignal()
        if(data["action"] == "sell" or data["action"] == "strongsell"):
            bmex.sellSignal()

    else:
        bmex.sellSignal()
    return Response(status=200)



# WEB INTERFACE

@app.route("/", methods=['POST', 'GET'])
def index():
    '''
    index page for changing the settings
    '''

    return render_template('index.html')



if __name__ == "__main__":

    if len(sys.argv) > 1:
        portNumber = sys.argv[1]
    else:
        portNumber = 4040


    app.run(port=portNumber, debug=True)


