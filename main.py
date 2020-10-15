from flask import Flask, request, Response
from pyngrok import ngrok
import json
import ast


def parse_webhook(webhook_data):
    """
    This function takes the string from tradingview and turns it into a python dict.
    :param webhook_data: POST data from tradingview, as a string.
    :return: Dictionary version of string.
    """

    data = ast.literal_eval(webhook_data)
    return data


app = Flask(__name__)


@app.route('/')
def root():
    return 'online'


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = parse_webhook(request.get_data)
        print (data)
        return Response(status=200)


if __name__ == "__main__":
    app.run(port=5050, debug=True)
