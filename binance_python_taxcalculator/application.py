from flask import Flask, jsonify, render_template, request
from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
import re
import helper



app = Flask(__name__)

web3 = Web3(HTTPProvider(
    'https://mainnet.infura.io/v3/1bb497538b3a4553892b9f48b705f81d'))


@app.route("/")
def index():
    '''
    landing page 
    '''
    block = web3.eth.getBlock('latest')
    return render_template('index.html', blockNR = block['number'], minerNR = block['miner'])


@app.route('/create_key', methods = ['Get', 'post'])
def create_key():
    '''
    page for storing user submitted api keypair as json together with username
        args: none
        returns: flask template "create_key.html"
    '''
    
    if request.method == 'POST': #if the user has posted account data@
        address = request.form.to_dict() #collect data
        helper.make_user(address) #helper function to store userdata in mongodb atlas instance
        
        return render_template('create_key.html', address = address)

    return render_template('create_key.html')



if __name__ == "__main__":
    app.run(port = 8888, debug=True)
