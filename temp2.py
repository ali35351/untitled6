import pandas
import plotly.graph_objects as go

from indicators import Indicators

dataframes = {}

# df = pandas.read_csv('1h.csv')

candels_h1=Indicators.get_candels('1h.txt')
candels_h6=Indicators.candels_change(candels_h1,6)

df=pandas.DataFrame(candels_h6)

df['20sma'] = df['close'].rolling(window=20).mean()
df['stddev'] = df['close'].rolling(window=20).std()
df['lower_band'] = df['20sma'] - (1.5 * df['stddev'])
df['upper_band'] = df['20sma'] + (1.5 * df['stddev'])

df['TR'] = df['high'] - df['low']
df['ATR'] = df['TR'].rolling(window=20).mean()

df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.5)
df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.5)


def in_squeeze(df):
    return df['lower_band'] > df['lower_keltner'] and df['upper_band'] < df['upper_keltner']


df['squeeze_on'] = df.apply(in_squeeze, axis=1)

if df.iloc[-3]['squeeze_on'] and not df.iloc[-1]['squeeze_on']:
    print("{} is coming out the squeeze")

# save all dataframes to a dictionary
# we can chart individual names below by calling the chart() function
dataframes['BTC'] = df


def chart(df):
    candlestick = go.Candlestick(x=df['open_time'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])
    upper_band = go.Scatter(x=df['open_time'], y=df['upper_band'], name='Upper Bollinger Band', line={'color': 'red'})
    lower_band = go.Scatter(x=df['open_time'], y=df['lower_band'], name='Lower Bollinger Band', line={'color': 'red'})

    upper_keltner = go.Scatter(x=df['open_time'], y=df['upper_keltner'], name='Upper Keltner Channel',
                               line={'color': 'blue'})
    lower_keltner = go.Scatter(x=df['open_time'], y=df['lower_keltner'], name='Lower Keltner Channel',
                               line={'color': 'blue'})

    fig = go.Figure(data=[candlestick, upper_band, lower_band, upper_keltner, lower_keltner])
    fig.layout.xaxis.type = 'category'
    fig.layout.xaxis.rangeslider.visible = False
    fig.show()


df = dataframes['BTC']
chart(df)

# print(dict(df['squeeze_on']))

print(df.iloc[-3]['squeeze_on'])
print(df.iloc[-1]['squeeze_on'])

if not df.iloc[-3]['squeeze_on'] and df.iloc[-1]['squeeze_on']:
    print("{} is coming out the squeeze")