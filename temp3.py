import json
import time

import requests

# first=1_525_203_000_000
first=1_502_942_400_000
# end=1_602_422_700_000
# distance=97,138,800,000
for i in range(1660):
    s1=time.time()
    first+=60_000_000
    second=first+60_000_000-1
    req = requests.get('https://api.binance.com/api/v1/klines?symbol=ETHUSDT&interval=1m&startTime='+str(first)+'&endTime='+str(second)+'&limit=1000')
    json1=json.loads(req.text)
    with open('1me.csv','a') as f:
        for j in json1:
            f.write(str(j[0])+','+str(j[1])+','+str(j[2])+','+str(j[3])+','+str(j[4])+','+str(j[5])+','+str(j[6])+'\n')
    s2=time.time()-s1
    if s2<1:
        time.sleep(1-s2)


# import datetime
# s = "02/05/2018"
# print(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))