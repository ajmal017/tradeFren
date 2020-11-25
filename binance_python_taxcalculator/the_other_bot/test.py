import json
import requests
import time
import hashlib
import config

test = requests.get("https://api.binance.com/api/v1/ping")
servertime = requests.get("https://api.binance.com/api/v1/time")

servertimeobject = json.loads(servertime.text)
servertimeint = servertimeobject['serverTime']
hashedsig = hashlib.sha256(str(config.API_SECRET).encode('utf-8'))


userdata = requests.get("https://api.binance.com/api/v3/account",
                        params={
                            "signature": hashedsig,
                            "timestamp": servertimeint,
                        }
                        ,
                        headers={
                            "X-MBX-APIKEY": config.API_ID,
                        }
                        )
print(userdata)
