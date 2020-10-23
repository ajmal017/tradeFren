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
        data = request.get_json()
        tview.analyse_alert(data)
        print (data)

        bmexClient.buySignal(data)

        return Response(status=200)




if __name__ == "__main__":
    bmexClient = bmex.run()
    app.run(port=5050, debug=True)


