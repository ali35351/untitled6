import json
import time
from threading import Thread

import bybit
import requests

# Pair configs
conf_file_url = 'btc_config.txt'
# orders_file_url = 'd:\\1.txt'
orders_file_url = 'btc_orders.txt'

# app configs
new_orders = []
open_orders = []
prices = []
candels_1m = []
candels_15m = []
candels_30m = []
candels_1h = []
candels_2h = []
candels_4h = []
candels_6h = []
candels_12h = []
candels_1D = []
candels_1W = []
candels_1M = []

conf_dictionary = dict([])


def price_ticker(prices: list):
    i = 0
    print('price ticker is running')
    while True:
        try:
            s = time.time()
            req = requests.get('https://api.bybit.com/v2/public/tickers')

            s2 = time.time()
            jsonobj = json.loads(req.text)
            prices.append((float(jsonobj['result'][0]['last_price']),  # BTC
                           float(jsonobj['result'][1]['last_price']),  # ETH
                           float(jsonobj['result'][2]['last_price']),  # EOS
                           float(jsonobj['result'][3]['last_price']),  # XRP
                           float(jsonobj['result'][4]['last_price']),  # BTCUSDT
                           float(jsonobj['time_now'])))
            if s2 - s < 1:
                time.sleep(s2 - s)
        except Exception as e:
            print(e.args)

        i += 1
        if i > 1000000:
            del prices[0]


# def candel_loader():
#     req = requests.get('https://api.bybit.com/v2/public/tickers?symbol=' + Pair)
#     jsonobj = json.loads(req.text)
#     first_of_all = float(jsonobj['time_now'])
#     first = int(first_of_all - 10000)
#     for i in range(50):
#         url = 'https://api.bybit.com/v2/public/kline/list?symbol=' + Pair + '&interval=1&limit=200&from=' + str(first)
#         req = requests.get(url)
#         jsonobj = json.loads(req.text)
#         if jsonobj['result'] == None:
#             return
#         for dic_object in jsonobj['result']:
#             temp_candel = {'open_time': float(dic_object['open_time']), 'open': float(dic_object['open']),
#                            'high': float(dic_object['high']), 'low': float(dic_object['low']),
#                            'close': float(dic_object['close']), 'vol': float(dic_object['volume']),
#                            }
#             candels_1m.append(temp_candel)
#         first += 200
#
#     # first=1_600_000_000


def conf_loader_order_loader(conf_dictionary: dict, new_orders: list):
    print('config and order loader is running')
    while True:
        with open(orders_file_url, 'r') as ordf:
            # print('opening order file')
            for line in ordf.readlines():
                jobj = json.loads(line[:-1])
                new_orders.append(jobj)
                print('order received')
                print(jobj)
        with open(orders_file_url, 'w') as f:
            f.write('')
            pass  # for fushing order file

        with open(conf_file_url, 'r') as conf_file:
            conf_lines = conf_file.readlines()
            for line in conf_lines:
                string1 = line.split(',')
                conf_dictionary[string1[0]] = string1[1][:-1]
        time.sleep(5)
        if conf_dictionary['close'] == '1':
            close_application()


def open_postion(position_direction, open_price, close_price, leverage, stop_lose, priority, Pair, order_type="Market"):
    # print('this object went in position ')
    # print(position_direction,str(open_price),str(close_price),str(leverage),str(stop_lose),str(priority))
    client = bybit.bybit(test=False, api_key=conf_dictionary['api_key'], api_secret=conf_dictionary['api_secret'])
    coin = ''
    price_coin = 0
    if Pair == 'BTCUSD':
        coin = 'BTC'
        price_coin = 0
    elif Pair == 'ETHUSD':
        coin = 'ETH'
        price_coin = 1
    elif Pair == 'EOSUSD':
        coin = 'EOS'
        price_coin = 2
    elif Pair == 'XRPUSD':
        coin = 'XRP'
        price_coin = 3
    elif Pair == 'BTCUSDT':
        coin = 'BTC'
        price_coin = 4

    blc = client.Wallet.Wallet_getBalance(coin=coin).result()
    blc = blc[0]['result']['XRP']['equity']
    # print(leverage * 0.98 * blc * prices[-1][price_coin])
    # print()
    client.Positions.Positions_saveLeverage(symbol=Pair, leverage=str(leverage)).result()
    print(client.Order.Order_newV2(side=position_direction, symbol=Pair, order_type="Market",
                                   time_in_force="GoodTillCancel",
                                   qty=leverage * 0.98 * blc * prices[-1][price_coin],
                                   ).result())
    client.Positions.Positions_tradingStop(symbol=Pair, stop_loss=str(stop_lose), trailing_stop="0",
                                           new_trailing_active="0").result()

    if position_direction == 'Buy':
        rev = 'Sell'
    else:
        rev = 'Buy'
    print(client.Order.Order_newV2(side=rev, symbol=Pair, order_type="Limit",
                                   qty=leverage * 0.98 * blc * prices[-1][price_coin],
                                   price=close_price, time_in_force="GoodTillCancel").result())

    print('position opend')
    print(position_direction, str(open_price), str(close_price), str(leverage), str(stop_lose), str(priority))


def check_triger(price_value, triger_string):
    if triger_string[-1] == 'u':
        if price_value > float(triger_string[:-1]):
            return True
        else:
            return False
    elif triger_string[-1] == 'd':
        if price_value < float(triger_string[:-1]):
            return True
        else:
            return False
    else:
        return False


def order_manager(new_orders: list, open_orders: list):
    print('order manager is running')
    i = 0
    time.sleep(5)
    while True:
        s1 = time.time()
        for order_obj in new_orders:

            price_coin = 0
            if order_obj['Pair'] == 'BTCUSD':
                price_coin = 0
            elif order_obj['Pair'] == 'ETHUSD':
                price_coin = 1
            elif order_obj['Pair'] == 'EOSUSD':
                price_coin = 2
            elif order_obj['Pair'] == 'XRPUSD':
                price_coin = 3
            elif order_obj['Pair'] == 'BTCUSDT':
                price_coin = 4

            if check_triger(prices[-1][price_coin], order_obj['cancel_triger']):
                new_orders.remove(order_obj)
                print('this object was remove by cancel_triger 1')
                print(order_obj)
                continue
            if order_obj['cancel_triger_count'] == '2':
                if check_triger(prices[-1][price_coin], order_obj['cancel_triger2']):
                    new_orders.remove(order_obj)
                    print('this object was remove by cancel_triger 2 ')
                    print(order_obj)
                    continue

            if order_obj['triger_count'] == '1':
                if check_triger(prices[-1][price_coin], order_obj['triger1']):
                    new_orders.remove(order_obj)
                    print('this order went into position')
                    print(order_obj)
                    open_postion(order_obj['position_direction'], 1,
                                 float(order_obj['close1']),
                                 float(order_obj['stop_lose']), float(order_obj['leverage']),
                                 float(order_obj['priority']), order_obj['Pair'])
                    continue
            elif order_obj['triger_count'] == '2':
                if order_obj['triger1'] == 'filled':
                    if check_triger(prices[-1][price_coin], order_obj['triger2']):
                        new_orders.remove(order_obj)
                        print('this order went into position')
                        print(order_obj)
                        open_postion(order_obj['position_direction'], 1,
                                     float(order_obj['close1']),
                                     float(order_obj['stop_lose']), float(order_obj['leverage']),
                                     float(order_obj['priority']), order_obj['Pair'])
                        continue
                else:
                    if check_triger(prices[-1][price_coin], order_obj['triger1']):
                        order_obj['triger1'] = 'filled'
                        # print('triger1 was filled')
                        continue
        i += 1
        if i == 60:
            i = 0
            print(new_orders)
            # print(open_orders)

        s2 = time.time()
        temp = s2 - s1
        if temp < 1:
            time.sleep(1 - temp)


def close_application():
    if len(open_orders) == 0:
        exit()
    if conf_dictionary['close'] == 2:
        # close all open orders
        pass


conf_loader_thread = Thread(target=conf_loader_order_loader, args=[conf_dictionary, new_orders, ])
conf_loader_thread.start()

price_ticker_thread = Thread(target=price_ticker, args=[prices, ])
price_ticker_thread.start()
#
# candel_loader()
# print(candels_1m)
# print(prices[-10:])

order_manager_thread = Thread(target=order_manager, args=[new_orders, open_orders, ])
order_manager_thread.start()
