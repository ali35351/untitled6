import json

import requests

req = requests.get(
    'https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1h&limit=1000')
json1 = json.loads(req.text)
x=y=color1=[]
# t,o,h,l,c,v
open_time=[]
open1=[]
high1=[]
low1=[]
close1=[]
vol1=[]
for j in json1:
    open_time.append(j[0])
    open1.append(j[1])
    high1.append(j[2])
    low1.append(j[3])
    close1.append(j[4])
    vol1.append(j[5])

y.append(open1[0])
x.append(open_time[0])
color1.append('green')

low=low1[-1]
high=high1[-1]

for i in range(1,len(open1)):
    if open1[i]>close1[i]:
        if color1[-1]=='red':
            low=min(low,low[i])
        else:
            y.append(high)
        color1.append('red')

    else:
        color1.append('green')

    if color1[-2]==color1[-1] and color1[-1]=='green':
        high=max()
