from datetime import datetime
import backtrader as bt

class MCross(bt.SignalStrategy):

  def __init__(self):
    self.mfast, self.mwfast = 12, 12*4
    self.mslow, self.mwslow = 26, 26*4
    self.msignal, self.mwsignal = 9, 9*4
    self.macd = bt.indicators.MACDHisto(self.data,
                                   period_me1=self.mwfast,
                                   period_me2=self.mwslow,
                                   period_signal=self.mwsignal)
    ema1 = bt.ind.EMA(period=self.mwfast)
    ema2 = bt.ind.EMA(period=self.mwslow)
    self.cross = bt.ind.CrossOver(ema1, ema2)

  def next(self):
    if self.cross > 0:
      print('buy at {} in {}!'.format(self.data.datetime.date(), self.cross.data[0]))

    if self.cross < 0:
      print('sell at {} in {}!'.format(self.data.datetime.date(), self.cross.data[0]))


ticker = 'PDD'
fromdate = datetime(2019, 1, 1)
todate = datetime(2020, 10, 31)

cerebro = bt.Cerebro()
data = bt.feeds.YahooFinanceData(dataname=ticker, fromdate=fromdate,
                                  todate=todate)
cerebro.adddata(data) 

cerebro.addstrategy(MCross)
cerebro.run()
cerebro.plot()
