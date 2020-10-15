from flask import Flask, request, Response
from pyngrok import ngrok
import json
import ast


app = Flask(__name__)


@app.route('/')
def root():
    return 'online'


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        #data = ast.literal_eval(request.get_data(as_text=True))
        data = request.get_json()
        print (data)
        print (data.keys())
        return Response(status=200)


if __name__ == "__main__":
    app.run(port=5050, debug=True)
