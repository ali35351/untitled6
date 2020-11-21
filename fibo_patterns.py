def gartley(x, a, b, c, d, pair):
    if a > x:  # bullish
        temp1 = a - x
        temp2 = a - b
        temp1_min = temp1 * .618
        temp1_max = temp1 * .786
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not gartley')
            return

        temp1 = a - b
        temp2 = c - b
        temp1_min = temp1 * .382
        temp1_max = temp1
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not gartley')
            return

        is_g = True
        temp1 = c - b
        temp2 = c - d
        temp1_min = temp1 * 1.272
        temp1_max = temp1 * 2.618
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not gartley')
            is_g = False

        temp3 = a - x
        temp4 = a - d
        temp3_min = temp3 * .786
        temp3_max = temp3 * .886
        if temp4 < temp3_min or temp4 > temp3_max:
            is_g = False

        min_number = max(a - temp3_max, c - temp1_max)
        max_number = min(a - temp3_min, c - temp1_min)
        if (min_number > max_number):
            print('its not possible this pattern be gartley')
            return
        else:
            with open('manual_order.txt', 'a') as f:
                position = 'Buy'
                triger_count = "2"
                cancel_tirger2 = str(c) + 'u'
                cancel_triger_count = '2'
                cancel_tirger1 = str(min_number) + 'd'
                triger = str(max_number)
                stop_lose = str(round(min_number,4))
                triger1 = triger + 'd'
                triger2 = triger + 'u'

                if max_number > (1.618 * b - .618 * c):
                    close1 = str(round((1.014 * b - .014 * c),4))
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
                elif min_number < (1.618 * b - .618 * c):
                    close1 = str(round((1.3 * b - .3 * c),4))
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

                else:
                    close1 = str(round((1.3 * b - .3 * c),4))
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
                    close1 = str(round((1.014 * b - .014 * c),4))
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

        print('d must be between ' + str(min_number) + ' and ' + str(max_number))
        if (is_g):
            print('its a gartley go in posiotioin')
    else:  # bearish
        temp1 = x - a
        temp2 = b - a
        temp1_min = temp1 * .618
        temp1_max = temp1 * .786
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not gartley')
            return

        temp1 = b - a
        temp2 = b - c
        temp1_min = temp1 * .382
        temp1_max = temp1
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not gartley')
            return

        is_g = True
        temp1 = b - c
        temp2 = d - c
        temp1_min = temp1 * 1.272
        temp1_max = temp1 * 2.618
        if temp2 < temp1_min or temp2 > temp1_max:
            is_g = False

        temp3 = x - a
        temp4 = d - a
        temp3_min = temp3 * .786
        temp3_max = temp3 * .886
        if temp4 < temp3_min or temp4 > temp3_max:
            print('its not gartley')
            is_g = False

        min_number = max(a + temp3_min, c + temp1_min)
        max_number = min(a + temp3_max, c + temp1_max)
        if (min_number > max_number):
            print('its not possible this pattern be gartley')
            return
        else:
            with open('manual_order.txt', 'a') as f:
                position = 'Sell'
                triger_count = "2"
                cancel_tirger1 = str(max_number) + 'u'
                cancel_tirger2 = str(c) + 'd'
                cancel_triger_count = '2'
                triger = str(min_number)
                triger1 = triger + 'u'
                triger2 = triger + 'd'
                stop_lose = str(round(max_number,4))
                if max_number < (1.618 * b - .618 * c):
                    close1 = str(round((1.014 * b - .014 * c),4))
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
                elif min_number > (1.618 * b - .618 * c):
                    close1 = str(round((1.3 * b - .3 * c),4))
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
                else:
                    close1 = str(round((1.014 * b - .014 * c),4))
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

                    close1 = str(round((1.3 * b - .3 * c),4))
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

                # if d > (1.618 * b - .618 * c):
                #     triger = str(1.618 * b - .618 * c)
                #     triger1 = triger + 'u'
                #     triger2 = triger + 'd'
                #     close1 = str(round((1.3 * b - .3 * c)
                #     stop_lose = str(2.618 * b - 1.618 * c)
                #     f.write(
                #         '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
                # else:
                #     triger = str(1.272 * b - .272 * c)
                #     triger1 = triger + 'u'
                #     triger2 = triger + 'd'
                #     close1 = str(round((1.014 * b - .014 * c)
                #     stop_lose = str(1.618 * b - .618 * c)
                #     f.write(
                #         '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

        if (is_g):
            print('its a gartley go in posiotioin')
        print('d must be between ' + str(min_number) + ' and ' + str(max_number))


def bat(x, a, b, c, d, pair):
    if a > x:
        temp1 = a - x
        temp2 = a - b
        temp1_min = temp1 * .38
        temp1_max = temp1 * .618
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not bat')
            return

        temp1 = a - b
        temp2 = c - b
        temp1_min = temp1 * .38
        temp1_max = temp1
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not bat')
            return

        is_g = True
        temp1 = c - b
        temp2 = c - d
        temp1_min = temp1 * 1.618
        temp1_max = temp1 * 3.618
        if temp2 < temp1_min or temp2 > temp1_max:
            is_g = False

        temp3 = a - x
        temp4 = a - d
        temp3_min = temp3 * .886
        temp3_max = temp3
        if temp4 < temp3_min or temp4 > temp3_max:
            print('its not bat')
            is_g = False

        min_number = max(a - temp3_max, c - temp1_max)
        max_number = min(a - temp3_min, c - temp1_min)
        if (min_number > max_number):
            print('its not possible this pattern be bat')
            return
        else:
            position = 'Buy'
            triger_count = "2"
            cancel_tirger1 = str(min_number) + 'd'
            cancel_tirger2 = str(c) + 'u'
            cancel_triger_count = '2'
            triger = str(max_number)
            triger1 = triger + 'd'
            triger2 = triger + 'u'
            stop_lose = str(round(min_number,4))
            if min_number > (2.618 * b - 1.618 * c):
                close1 = str(round((1.63 * b - .63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

            elif max_number < (2.618 * b - 1.618 * c):
                close1 = str(round((1.63 * b - .63*c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
            else:
                close1 = str(round((1.3 * b - .3 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
                close1 = str(round((1.63 * b - .63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')


        print('d must be between ' + str(min_number) + ' and ' + str(max_number))
        if (is_g):
            print('its a bat go in posiotioin')

    else:
        temp1 = x - a
        temp2 = b - a
        temp1_min = temp1 * .38
        temp1_max = temp1 * .618
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not bat')
            return

        temp1 = b - a
        temp2 = b - c
        temp1_min = temp1 * .38
        temp1_max = temp1
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not bat')
            return

        is_g = True
        temp1 = b - c
        temp2 = d - c
        temp1_min = temp1 * 1.618
        temp1_max = temp1 * 3.618
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not bat')
            is_g = False

        temp3 = x - a
        temp4 = d - a
        temp3_min = temp3 * .886
        temp3_max = temp3
        if temp4 < temp3_min or temp4 > temp3_max:
            print('its not bat')
            is_g = False

        min_number = max(a + temp3_min, c + temp1_min)
        max_number = min(a + temp3_max, c + temp1_max)
        if (min_number > max_number):
            print('its not possible this pattern be bat')
            return
        else:
            position = 'Sell'
            triger_count = "2"
            cancel_tirger1 = str(max_number) + 'u'
            cancel_tirger2 = str(c) + 'd'
            cancel_triger_count = '2'
            triger = str(min_number)
            triger1 = triger + 'u'
            triger2 = triger + 'd'
            stop_lose = str(round(max_number,4))
            if max_number < (2.618 * b - 1.618 * c):
                close1 = str(round((1.3 * b - .3 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')


            elif min_number > (2.618 * b - 1.618 * c):
                close1 = str(round((1.63 * b - .63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

            else:
                close1 = str(round((1.3 * b - .3 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
                close1 = str(round((1.63 * b - .63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

        print('d must be between ' + str(min_number) + ' and ' + str(max_number))
        if (is_g):
            print('its a bat go in posiotioin')


def crab(x, a, b, c, d, pair):
    if a > x:
        temp1 = a - x
        temp2 = a - b
        temp1_min = temp1 * .382
        temp1_max = temp1 * .786
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not crab')
            return

        temp1 = a - b
        temp2 = c - b
        temp1_min = temp1 * .382
        temp1_max = temp1
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not crab')
            return

        is_g = True
        temp1 = c - b
        temp2 = c - d
        temp1_min = temp1 * 2.24
        temp1_max = temp1 * 4.236
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not crab')
            is_g = False

        temp3 = a - x
        temp4 = a - d
        temp3_min = temp3 * 1.618
        temp3_max = temp3 * 2.618
        if temp4 < temp3_min or temp4 > temp3_max:
            print('its not crab')
            is_g = False

        min_number = max(a - temp3_max, c - temp1_max)
        max_number = min(a - temp3_min, c - temp1_min)
        if min_number > max_number:
            print('its not possible to be a crab pattern')
            return
        else:
            position = 'Buy'
            triger_count = "2"
            cancel_tirger1 = str(max_number) + 'd'
            cancel_tirger2 = str(c) + 'u'
            cancel_triger_count = '2'
            triger = str(min_number)
            triger1 = triger + 'd'
            triger2 = triger + 'u'
            stop_lose = str(round(max_number,4))
            if max_number > (3.618 * b - 2.618 * c):
                close1 = str(round((2.63 * b - 1.63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

            elif min_number < (3.618 * b - 2.618 * c):
                close1 = str(round((1.63 * b - .63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
            else:
                close1 = str(round((1.63 * b - .63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
                close1 = str(round((2.63 * b - 1.63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

        if (is_g):
            print('its a crab go in posiotioin')
        print('d must be between ' + str(min_number) + ' and ' + str(max_number))
    else:
        temp1 = x - a
        temp2 = b - a
        temp1_min = temp1 * .382
        temp1_max = temp1 * .786
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not crab')
            return

        temp1 = b - a
        temp2 = b - c
        temp1_min = temp1 * .382
        temp1_max = temp1
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not crab')
            return

        is_g = True
        temp1 = b - c
        temp2 = d - c
        temp1_min = temp1 * 2.24
        temp1_max = temp1 * 4.236
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not crab')
            is_g = False

        temp3 = x - a
        temp4 = d - a
        temp3_min = temp3 * 1.618
        temp3_max = temp3 * 2.618
        if temp4 < temp3_min or temp4 > temp3_max:
            print('its not crab')
            is_g = False

        min_number = max(a + temp3_min, c + temp1_min)
        max_number = min(a + temp3_max, c + temp1_max)

        if min_number > max_number:
            print('its not possible to be a crab pattern')
            return
        else:
            position = 'Sell'
            triger_count = "2"
            cancel_tirger1 = str(max_number) + 'u'
            cancel_tirger2 = str(c) + 'd'
            cancel_triger_count = '2'
            triger = str(min_number)
            triger1 = triger + 'u'
            triger2 = triger + 'd'
            stop_lose = str(round(max_number,4))
            if max_number > (3.618 * b - 2.618 * c):
                close1 = str(round((2.63 * b - 1.63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

            elif min_number < (3.618 * b - 2.618 * c):
                close1 = str(round((1.63 * b - .63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
            else:
                close1 = str(round((1.63 * b - .63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
                close1 = str(round((2.63 * b - 1.63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

        if (is_g):
            print('its a crab go in posiotioin')
        print('d must be between ' + str(min_number) + ' and ' + str(max_number))


def butterfly(x, a, b, c, d, pair):
    if a > x:
        temp1 = a - x
        temp2 = a - b
        temp1_min = temp1 * .782
        temp1_max = temp1 * .886
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not butterfly')
            return

        temp1 = a - b
        temp2 = c - b
        temp1_min = temp1 * .382
        temp1_max = temp1
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not butterfly')
            return

        is_g = True
        temp1 = c - b
        temp2 = c - d
        temp1_min = temp1 * 1.618
        temp1_max = temp1 * 3.618
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not butterfly')
            is_g = False

        temp3 = a - x
        temp4 = a - d
        temp3_min = temp3 * 1.272
        temp3_max = temp3 * 2.618
        if temp4 < temp3_min or temp4 > temp3_max:
            print('its not butterfly')
            is_g = False

        min_number = max(a - temp3_max, c - temp1_max)
        max_number = min(a - temp3_min, c - temp1_min)

        if (min_number > max_number):
            print('its not possible this pattern be bat')
            return
        else:
            position = 'Buy'
            triger_count = "2"
            cancel_tirger1 = str(max_number) + 'd'
            cancel_tirger2 = str(c) + 'u'
            cancel_triger_count = '2'
            triger = str(min_number)
            triger1 = triger + 'd'
            triger2 = triger + 'u'
            stop_lose = str(round(max_number,4))
            if max_number > (2.618 * b - 1.618 * c):
                close1 = str(round((1.3 * b - .3 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

            elif min_number < (2.618 * b - 1.618 * c):
                close1 = str(round((1.63 * b - .63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
            else:
                close1 = str(round((1.3 * b - .3 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
                close1 = str(round((1.63 * b - .63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

        if (is_g):
            print('its a butterfly go in posiotioin')
        print('d must be between ' + str(min_number) + ' and ' + str(max_number))
    else:
        temp1 = x - a
        temp2 = b - a
        temp1_min = temp1 * .782
        temp1_max = temp1 * .886
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not butterfly')
            return

        temp1 = b - a
        temp2 = b - c
        temp1_min = temp1 * .382
        temp1_max = temp1
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not butterfly')
            return

        is_g = True
        temp1 = b - c
        temp2 = d - c
        temp1_min = temp1 * 1.618
        temp1_max = temp1 * 3.618
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not butterfly')
            is_g = False

        temp3 = x - a
        temp4 = d - a
        temp3_min = temp3 * 1.272
        temp3_max = temp3 * 2.618
        if temp4 < temp3_min or temp4 > temp3_max:
            print('its not butterfly')
            is_g = False

        min_number = max(a + temp3_min, c + temp1_min)
        max_number = min(a + temp3_max, c + temp1_max)

        if (min_number > max_number):
            print('its not possible this pattern be bat')
            return
        else:
            position = 'Sell'
            triger_count = "2"
            cancel_tirger1 = str(max_number) + 'u'
            cancel_tirger2 = str(c) + 'd'
            cancel_triger_count = '2'
            triger = str(min_number)
            triger1 = triger + 'u'
            triger2 = triger + 'd'
            stop_lose = str(round(max_number,4))
            if max_number < (2.618 * b - 1.618 * c):
                close1 = str(round((1.3 * b - .3 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')


            elif min_number > (2.618 * b - 1.618 * c):
                close1 = str(round((1.63 * b - .63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

            else:
                close1 = str(round((1.3 * b - .3 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')
                close1 = str(round((1.63 * b - .63 * c),4))
                with open('manual_order.txt', 'a') as f:
                    f.write(
                        '{"position_direction":"' + position + '", "triger_count": "' + triger_count + '", "triger1": "' + triger1 + '", "triger2": "' + triger2 + '", "close1": "' + close1 + '", "priority": "12", "leverage": "10", "stop_lose": "' + stop_lose + '", "cancel_triger": "' + cancel_tirger1 + '", "cancel_triger2": "' + cancel_tirger2 + '", "cancel_triger_count": "' + cancel_triger_count + '", "Pair": "' + pair + '"}' + '\n')

        if (is_g):
            print('its a butterfly go in posiotioin')
        print('d must be between ' + str(min_number) + ' and ' + str(max_number))


def three_drive_pattern(x, a, b, c, d, pair):  # stop lose is 161 percent of second drive
    if a > x:
        temp1 = a - x
        temp2 = a - b
        temp1_min = temp1 * 1.27
        temp1_max = temp1 * 2.61
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not 3 drive')
            return

        temp1 = c - b
        temp2 = c - d
        temp1_min = temp1 * 1.27
        temp1_max = temp1 * 2.61
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not 3 drive')
            print('d must be between ' + str(c - temp1_min) + ' and ' + str(c - temp1_max))
            return

        print('its bullish 3 dirve pattern go in position')
        print('d must be between ' + str(c - temp1_min) + ' and ' + str(c - temp1_max))
    else:
        temp1 = x - a
        temp2 = b - a
        temp1_min = temp1 * 1.27
        temp1_max = temp1 * 2.61
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not 3 drive')
            return

        temp1 = b - c
        temp2 = d - c
        temp1_min = temp1 * 1.27
        temp1_max = temp1 * 2.61
        if temp2 < temp1_min or temp2 > temp1_max:
            print('its not 3 drive')
            print('d must be between ' + str(c + temp1_min) + ' and ' + str(c + temp1_max))
            return
        print('its bearish 3 drive pattern fo in possiotion')
        print('d must be between ' + str(c + temp1_min) + ' and ' + str(c + temp1_max))


# three_drive_pattern(10000,11000,9400,10300,8000)
# gartley(15951.24, 15407.10, 15749.12, 15475.83, 15855.17)
# bat(.28024,.22420,.25483,.23528,.27655)

def abcd(a, b, c, d):
    if a > b:
        temp_min = (a - b) * 0.618
        temp_max = (a - b) * .886
        temp_c = c - b
        first_wave = False
        if temp_c < temp_max and temp_c > temp_min:
            first_wave = True
        temp_min = (c - b) * 1.27
        temp_max = (c - b) * 2
        temp_d = (c - d)
        second_wave = False
        if temp_d < temp_max and temp_d > temp_min:
            second_wave = True
        if first_wave and second_wave:
            print('its abcd')
    else:
        temp_min = (b - a) * 0.618
        temp_max = (b - a) * .886
        temp_c = b - c
        first_wave = False
        if temp_c < temp_max and temp_c > temp_min:
            first_wave = True
        temp_min = (b - c) * 1.27
        temp_max = (b - c) * 2
        temp_d = (d - c)
        second_wave = False
        if temp_d < temp_max and temp_d > temp_min:
            second_wave = True
        if first_wave and second_wave:
            return True


def is_a_patter(x, a, b, c, d, pair):
    print('gartley:')
    gartley(x, a, b, c, d, pair)
    print('bat:')
    bat(x, a, b, c, d, pair)
    print('butterfly:')
    butterfly(x, a, b, c, d, pair)
    print('carb:')
    crab(x, a, b, c, d, pair)
    if abcd(a, b, c, d):
        print('its abcd')
    else:
        print('its not abcd')


is_a_patter(0.2776, 0.2617, 0.2707, 0.2621, 0.2771, 'XRPUSD')
