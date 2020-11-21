import json

import requests

Pair = 'BTCUSD'

url = 'https://api.bybit.com/v2/public/kline/list?symbol=' + Pair + '&interval=1&limit=200&from=' + str(1600000000)
req = requests.get(url)
jsonobj = json.loads(req.text)
for dic_object in jsonobj['result']:
    temp_candel = {'open_time': float(dic_object['open_time']), 'open': float(dic_object['open']),
                   'high': float(dic_object['high']), 'low': float(dic_object['low']),
                   'close': float(dic_object['close']), 'vol': float(dic_object['volume']),
                   }
    print(temp_candel)
