import statistics
import statistics as stats
import math as math

from matplotlib import pyplot
from matplotlib.patches import Rectangle


class Indicators:
    def get_candels(file_url: str):
        candels = []
        with open(file_url, 'r') as f:
            for line in f.readlines():
                s = line.split(',')
                candel = {
                    'open_time': float(s[0]),
                    'open': float(s[1]),
                    'high': float(s[2]),
                    'low': float(s[3]),
                    'close': float(s[4]),
                    'vol': float(s[5])
                }
                candels.append(candel)

        return candels

    def macd_line_signal_line(candels: list, num_periods_fast=12, num_periods_slow=26, num_periods_macd=9):
        # num_periods_fast = 10  # fast EMA time period
        K_fast = 2 / (num_periods_fast + 1)  # fast EMA smoothing factor
        ema_fast = 0
        # num_periods_slow = 40  # slow EMA time period
        K_slow = 2 / (num_periods_slow + 1)  # slow EMA smoothing factor
        ema_slow = 0

        # num_periods_macd = 20  # MACD EMA time period
        K_macd = 2 / (num_periods_macd + 1)  # MACD EMA smoothing factor
        ema_macd = 0

        ema_fast_values = []  # track fast EMA values for visualization purposes
        ema_slow_values = []  # track slow EMA values for visualization purposes
        macd_values = []  # track MACD values for visualization purposes
        macd_signal_values = []  # MACD EMA values tracker

        macd_histogram_values = []  # MACD - MACD-EMA

        for candel in candels:
            close_price = candel['close']
            if (ema_fast == 0):  # first observation
                ema_fast = close_price
                ema_slow = close_price
            else:
                ema_fast = (close_price - ema_fast) * K_fast + ema_fast
                ema_slow = (close_price - ema_slow) * K_slow + ema_slow

            ema_fast_values.append(ema_fast)
            ema_slow_values.append(ema_slow)
            macd = ema_fast - ema_slow  # MACD is fast_MA - slow_EMA

            if ema_macd == 0:
                ema_macd = macd
            else:
                ema_macd = (macd - ema_macd) * K_slow + ema_macd  # signal is EMA of MACD values

            macd_values.append(macd)
            macd_signal_values.append(ema_macd)
            macd_histogram_values.append(macd - ema_macd)
        return macd_values, macd_signal_values, macd_histogram_values

    def bollinger(candels: list, time_period=20, stdev_factor=2):
        # time_period = 20  # history length for Simple Moving Average for middle band
        # stdev_factor = 2  # Standard Deviation Scaling factor for the upper and lower bands
        history = []  # price history for computing simple moving average
        sma_values = []  # moving average of prices for visualization purposes
        upper_band = []  # upper band values
        lower_band = []  # lower band values

        for candel in candels:
            close_price = candel['close']
            history.append(close_price)
            if len(
                    history) > time_period:  # we only want to maintain at most 'time_period' number of price observations
                del (history[0])

            sma = stats.mean(history)
            sma_values.append(sma)  # simple moving average or middle band
            variance = 0  # variance is the square of standard deviation
            for hist_price in history:
                variance = variance + ((hist_price - sma) ** 2)

            stdev = math.sqrt(variance / len(history))  # use square root to get standard deviation

            upper_band.append(sma + stdev_factor * stdev)
            lower_band.append(sma - stdev_factor * stdev)
        return upper_band, lower_band

    def candels_change(candels: list, new_time=5):
        candels2 = []
        i = 0
        temp_candels = []
        for candel in candels:
            i += 1
            temp_candels.append(candel)
            if i == new_time:
                vol = 0
                for cd in temp_candels:
                    vol += cd['vol']
                temp_candel = {
                    'open_time': temp_candels[0]['open_time'],
                    'open': temp_candels[0]['open'],
                    'high': Indicators.candels_high(temp_candels),
                    'low': Indicators.candels_low(temp_candels),
                    'close': temp_candels[-1]['close'],
                    'vol': vol
                }
                candels2.append(temp_candel)
                temp_candels = []
                i = 0
        return candels2

    def ema(self, candels: list, num_periods):
        if num_periods == None:
            num_periods = 20  # number of days over which to average
        K = 2 / (num_periods + 1)  # smoothing constant
        ema_p = 0
        ema_values = []  # to hold computed EMA values

        for candel in candels:
            if (ema_p == 0):  # first observation, EMA = current-price
                ema_p = candel['close']
            else:
                ema_p = (candel['close'] - ema_p) * K + ema_p
            ema_values.append(ema_p)

        return ema_values

    def sma(candels: list, num_periods):
        if num_periods == None:
            num_periods = 20  # number of days over which to average

        sma_values = []  # to hold computed EMA values
        history = []
        for candel in candels:
            history.append(candel['close'])
            if len(
                    history) > num_periods:  # we remove oldest price because we only average over last 'time_period' prices
                del (history[0])

            sma_values.append(stats.mean(history))
        return sma_values

    def line_plot(candels: list):
        x = []
        y = []
        for candel in candels:
            x.append(candel['open_time'])
            y.append(candel['close'])
        pyplot.plot(x, y)
        pyplot.show()

    def chart_plot(candels: list):
        currentAxis = pyplot.gca()
        # max1 = candels[0]['close']
        # min1 = candels[0]['open']
        j = 100
        for i in candels:
            j += 1
            if i['color'] == 'green':
                currentAxis.add_patch(Rectangle((j, i['open']), 1, i['close'] - i['open'], facecolor="green"))
            else:
                currentAxis.add_patch(Rectangle((j, i['close']), 1, i['open'] - i['close'], facecolor="red"))
        currentAxis.set_xlim(99, 500)
        currentAxis.set_ylim(4000, 20000)
        pyplot.show()

    def candels_to_list(candels: list):
        open_times = []
        opens = []
        highs = []
        closes = []
        lows = []
        vols = []
        for candel in candels:
            open_times.append(candel['open_time'])
            opens.append(candel['open'])
            closes.append(candel['close'])
            highs.append(candel['high'])
            lows.append(candel['low'])
            vols.append(candel['vol'])
        return open_times, opens, highs, lows, closes, vols

    def candels_high(candels: list):
        h = 0
        for candel in candels:
            if candel['open'] > h:
                h = candel['open']
            if candel['close'] > h:
                h = candel['close']
        return h

    def candels_low(candels: list):
        l = 100000000000000
        for candel in candels:
            if candel['open'] < l:
                l = candel['open']
            if candel['close'] < l:
                l = candel['close']
        return l

    def candels_mean_std_range(candels: list):
        sum1 = 0
        sum2 = 0
        l = len(candels)
        if l == 0 or l == 1:
            return
        for candel in candels:
            sum1 += candel['close']
            sum2 += candel['high'] - candel['low']
        m = sum1 / l
        rm = sum2 / l
        stdev = 0
        for candel in candels:
            stdev += (m - candel['close']) ** 2
        stdev /= l - 1
        stdev = math.sqrt(stdev)

        return m, stdev, rm

    def candels_mean(candels: list):
        sum1 = 0
        l = len(candels)
        if l == 0:
            return 0
        for candel in candels:
            sum1 += candel['close']
        return sum1 / l

    # def keltnerChanels(candels: list, lengthKC, multKC):
    #     if len(candels) < lengthKC:
    #         return
    #     upperKC = []
    #     lowerKC = []
    #     if lengthKC == None:
    #         lengthKC = 20
    #     if multKC == None:
    #         multKC = 1.5
    #     for i in range(lengthKC, len(candels) + 1):
    #         ma = Indicators.candels_mean(candels[i - lengthKC:i], 'close')
    #         rangema = Indicators.candels_range_mean(candels[i - lengthKC:i])
    #
    #         upperKC.append(ma + rangema * multKC)
    #         lowerKC.append(ma - rangema * multKC)
    #
    #     return upperKC, lowerKC

    def ThreeLineBreak(candels: list):
        open_times, opens_list, highs, lows, close_list, vols = Indicators.candels_to_list(candels)
        three_line_break = []

        if len(opens_list) <= 10:
            return

        if opens_list[0] < close_list[0]:
            temp = {'open': opens_list[0], 'close': close_list[0], 'color': 'green'}
        else:
            temp = {'open': close_list[0], 'close': opens_list[0], 'color': 'red'}
        three_line_break.append(temp)
        three_line_break.append(temp)
        three_line_break.append(temp)

        for i in range(1, len(opens_list)):
            if three_line_break[-1]['color'] == 'green':
                if close_list[i] > three_line_break[-1]['close']:
                    three_line_break.append(
                        {'open': three_line_break[-1]['close'], 'close': close_list[i], 'color': 'green'})
                elif close_list[i] < Indicators.candels_low(three_line_break[-3:]):
                    three_line_break.append(
                        {'open': three_line_break[-1]['open'], 'close': close_list[i], 'color': 'red'})

            if three_line_break[-1]['color'] == 'red':
                if close_list[i] < three_line_break[-1]['close']:
                    three_line_break.append(
                        {'open': three_line_break[-1]['close'], 'close': close_list[i], 'color': 'red'})
                elif close_list[i] > Indicators.candels_high(three_line_break[-3:]):
                    three_line_break.append(
                        {'open': three_line_break[-1]['open'], 'close': close_list[i], 'color': 'green'})
        del three_line_break[:2]
        return three_line_break

    def renko(candels: list, pipsize: float):
        renko_list = []
        open_times, opens_list, highs_list, lows_list, close_list, vols = Indicators.candels_to_list(candels)
        if len(opens_list) <= 15:
            return
        list1 = [max(highs_list[i] - lows_list[i], abs(highs_list[i] - close_list[i - 1]),
                     abs(lows_list[i] - close_list[i - 1])) for i in range(-15, -1)]
        if pipsize == None:
            pipsize = sum(list1) / 14
            print(pipsize)

        if opens_list[0] < close_list[0]:
            temp = {'open': opens_list[0], 'close': close_list[0], 'color': 'green'}
        else:
            temp = {'open': close_list[0], 'close': opens_list[0], 'color': 'red'}
        renko_list.append(temp)
        for i in range(1, len(close_list)):
            if renko_list[-1]['color'] == 'green':
                if renko_list[-1]['close'] < close_list[i]:
                    las = renko_list[-1]['close']
                    for j in range(int((close_list[i] - las) / pipsize)):
                        open2 = renko_list[-1]['close']
                        close2 = open2 + pipsize
                        renko_list.append({'open': open2, 'close': close2, 'color': 'green'})

                if renko_list[-1]['open'] > close_list[i]:
                    las = renko_list[-1]['open']
                    for j in range(int((las - close_list[i]) / pipsize)):
                        if j == 0:
                            open2 = renko_list[-1]['open']
                        else:
                            open2 = renko_list[-1]['close']
                        close2 = open2 - pipsize
                        renko_list.append({'open': open2, 'close': close2, 'color': 'red'})

            if renko_list[-1]['color'] == 'red':
                if renko_list[-1]['close'] > close_list[i]:
                    las = renko_list[-1]['close']
                    for j in range(int((las - close_list[i]) / pipsize)):
                        open2 = renko_list[-1]['close']
                        close2 = open2 - pipsize
                        renko_list.append({'open': open2, 'close': close2, 'color': 'red'})

                if renko_list[-1]['open'] < close_list[i]:
                    las = renko_list[-1]['open']
                    for j in range(int((close_list[i] - las) / pipsize)):
                        if j == 0:
                            open2 = renko_list[-1]['open']
                        else:
                            open2 = renko_list[-1]['close']
                        close2 = open2 + pipsize
                        renko_list.append({'open': open2, 'close': close2, 'color': 'green'})
        del renko_list[0]
        return renko_list


class Strategy:
    def __init__(self, candels, init_value=100, taker_fee=0.00075, maker_fee=-0.00025):
        self.max_draw_down = 0
        self.win_trades = 0
        self.loss_trades = 0
        self.profit = 0
        self.init_value = init_value
        self.taker_fee = taker_fee
        self.maker_fee = maker_fee
        self.days = 0
        self.candels = candels
        self.my_candels = []
        self.final_value = 0
        self.buy_and_hold = 0
        self.position = 'flat'
        self.index = 0
        self.first_time = True

    def report(self):
        print('max_draw_down is : ', self.max_draw_down)
        print('win_trades is : ', self.win_trades)
        print('loss is : ', self.loss_trades)
        print('profit is : ', self.profit)
        print('init_value is : ', self.init_value)
        print('taker_fee is : ', self.taker_fee)
        print('maker_fee is : ', self.maker_fee)
        print('days is : ', self.days)
        print('final_value is : ', self.final_value)
        print('buy_and_hold is : ', self.buy_and_hold)

    def __str__(self):
        return str(self.max_draw_down) + ',' + str(self.win_trades) + ',' + str(self.loss_trades) + ',' + str(
            self.profit) + ',' + str(self.init_value) + ',' + str(self.taker_fee) + ',' + str(
            self.maker_fee) + ',' + str(self.days) + ',' + str(self.final_value) + ',' + str(self.buy_and_hold)

    def pre_strategy(self):
        self.days = self.candels[-1]['open_time'] - self.candels[0]['open_time']
        self.days = self.days / 86400
        self.buy_and_hold = self.candels[-1]['open'] - self.candels[0]['open']
        self.buy_and_hold = self.buy_and_hold / self.candels[-1]['open']
        self.final_value = self.init_value

    def close_position(self):
        positionded_price = self.my_candels[self.index]['close']
        current_price = self.my_candels[-1]['close']
        if self.position == 'long':
            profit = (current_price - positionded_price) / current_price
            profit -= self.taker_fee
            if profit < 0:
                self.loss_trades += 1
                self.max_draw_down = max(self.max_draw_down, abs(profit))
            else:
                self.win_trades += 1
            liquidity = Indicators.candels_low(self.my_candels[self.index + 1:])
            liquidity = (liquidity - positionded_price) / liquidity
            self.max_draw_down = max(self.max_draw_down, abs(liquidity))
            self.final_value = self.final_value + self.final_value * profit

        if self.position == 'short':
            profit = (positionded_price - current_price) / current_price
            profit -= self.taker_fee
            if profit < 0:
                self.loss_trades += 1
                self.max_draw_down = max(self.max_draw_down, abs(profit))
            else:
                self.win_trades += 1
            liquidity = Indicators.candels_high(self.my_candels[self.index + 1:])
            liquidity = (positionded_price - liquidity) / liquidity
            self.max_draw_down = max(self.max_draw_down, abs(liquidity))
            self.final_value = self.final_value + self.final_value * profit
        self.position = 'flat'
        print('position opend at', positionded_price, 'closed at', current_price)


class ThreeLineBreakStrategy(Strategy):
    def do_trades(self):
        self.pre_strategy()


class TTMSqeezeStrategy(Strategy):
    def __init__(self, candels, bbLenth, bbDev, ktLength, ktMul):
        super().__init__(candels)
        self.bbLength = bbLenth
        self.bbDev = bbDev
        self.ktLength = ktLength
        self.ktMul = ktMul

    def do_trades(self):
        self.pre_strategy()
        squeeze = []
        for candel in self.candels:
            self.my_candels.append(candel)
            if len(self.my_candels) < 20:
                continue

            m1,st1,rm1=Indicators.candels_mean_std_range(self.my_candels[-self.bbLength:])
            sqzOn=st1*self.bbDev<=rm1*self.ktMul

            squeeze.append(sqzOn)
            if sqzOn:  # black
                if not self.position == 'flat':
                    self.close_position()
            else:  # gray
                if True not in squeeze:
                    continue
                else:
                    if self.my_candels[-12]['close'] > self.my_candels[-1]['close']:
                        # go short
                        self.index = len(self.my_candels) - 1
                        self.position = 'short'
                        pass
                    else:
                        # go long
                        self.index = len(self.my_candels) - 1
                        self.position = 'long'
                        pass
        print(squeeze)
        self.profit=(self.final_value-self.init_value)/self.init_value


# class MohsenStrategy(Strategy):
#     def __init__(self, candels, fast, slow, uslow):
#         super().__init__(candels)
#         self.fast=fast
#         self.slow=slow
#         self.uslow=uslow
#
#     def do_trade(self):
#         self.pre_strategy()
#         ma1=[]
#         ma4=[]
#         ma24=[]
#         buy_price=0
#         first_creation=True
#         position='flat'
#         for candel in self.candels:
#             self.my_candels.append(candel)
#             if len(self.my_candels)<24:
#                 continue
#             ma1.extend(Indicators.sma(self.my_candels[-self.fast:],self.fast))
#             ma4.extend(Indicators.sma(self.my_candels[-self.slow:],self.slow))
#             ma24.extend(Indicators.sma(self.my_candels[-self.uslow:],self.uslow))
#             if first_creation:
#                 first_creation=False
#                 continue
#             if ma24[-1]<ma24[-2] and ma4[-1]>ma4[-2] and ma1[-1]<ma1[-2] and position=='flat' and candel['open']<candel['close']:
#                 position='long'
#                 buy_price=candel['close']
#             if ma1[-1]>ma1[-2] and position=='long':
#                 self.final_value+=self.final_value*(candel['close']-buy_price)/buy_price
#                 print(self.final_value)
#                 position='flat'
#
#
#
#         self.profit = (self.final_value - self.init_value) / self.init_value


# class Season_10Strategy(Strategy):
#