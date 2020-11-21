import indicators
from matplotlib import pyplot

candels1m = indicators.Indicators.get_candels('1m.txt')
candels1h=indicators.Indicators.candels_change(candels1m,60)
# candels1h=indicators.Indicators.candels_change(candels1h,6)

# open_times,opens,highs,closes,lows,vols=indicators.Indicators.candels_to_list(candels1h)
# # #
# kub,klb=indicators.Indicators.keltnerChanels(candels1h,20,1.5)
# bub,blb=indicators.Indicators.bollinger(candels1h,20,1.5)
# # #
# pyplot.plot(open_times,closes)
# pyplot.plot(open_times[19:],kub,'k')
# pyplot.plot(open_times[19:],klb,'k')
# pyplot.plot(open_times,bub,'r')
# pyplot.plot(open_times,blb,'r')
# pyplot.show()

ttm= indicators.TTMSqeezeStrategy(candels1h,20,2,20,1.5)
ttm.do_trades()
ttm.report()

# mohsen_s=indicators.MohsenStrategy(candels5m,12,48,288)
# mohsen_s.do_trade()
# mohsen_s.report()

# print(kub[-1])
# print(klb[-1])
# print(bub[-1])
# print(blb[-1])


# open_times,opens,highs,lows,closes,vols=indicators.Indicators.candels_to_list(candels1h)
# trend=[]
# for i in range(len(open_times)):
#     if opens[i]>closes[i]:
#         trend.append((lows[i]-opens[i])/lows[i])
#     else:
#         trend.append((highs[i]-opens[i])/highs[i])
#
# print(sorted(trend))

