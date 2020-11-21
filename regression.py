import pandas
from matplotlib import pyplot
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import indicators

candels = indicators.Indicators.get_candels('1h.txt')
# indicators.Indicators.line_plot(candels)

# candidates=dict([])
open_times, opens, highs, lows, closes, vols = indicators.Indicators.candels_to_list(candels)
cl=[]
for close in closes:
    cl.append(int(close))

closes=cl

candidates = {
    'open_time': open_times,
    'vol': vols,
    'close': closes
}

df = pandas.DataFrame(candidates, columns=['open_time', 'vol', 'close'])
# print(df)
X = df[['open_time']]
y = df['close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=0)
logistic_regression = LogisticRegression()
logistic_regression.fit(X_train, y_train)
y_pred = logistic_regression.predict(X_test)

print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))
print(y_test)
print(y_pred)
# pyplot.show()
