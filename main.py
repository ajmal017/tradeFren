from flask import Flask, request, Response
from pyngrok import ngrok
import json
import tradingview_adapter as tview
import bitmex_adapter as bmex


app = Flask(__name__)



@app.route('/')
def root():
    return 'online'


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




if __name__ == "__main__":
    app.run(port=4040, debug=True)


