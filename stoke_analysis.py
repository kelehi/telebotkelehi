from tradingview_ta import TA_Handler, Interval


class Moex_ta:
    def __init__(self, active: str, timeframe=None):
        self.active = active
        self.timeframe = timeframe

    def technical_analysis(self) -> str:
        interpreter = {'SELL': 'Продавать', 'BUY': 'Покупать', 'NEUTRAL': 'Нейтрально'}
        technical_analysis_ = self.time_frame()
        return interpreter[technical_analysis_]

    def time_frame(self) -> str:
        if self.timeframe == '1d' or self.timeframe is None:
            activ = TA_Handler(symbol=self.active,
                               screener='russia',
                               exchange='MOEX',
                               interval=Interval.INTERVAL_1_DAY)

            dict_recommendation = dict(activ.get_analysis().summary)
            return dict_recommendation['RECOMMENDATION']

        elif self.timeframe == '1m':
            activ = TA_Handler(symbol=self.active,
                               screener='russia',
                               exchange='MOEX',
                               interval=Interval.INTERVAL_1_MINUTE)

            dict_recommendation = dict(activ.get_analysis().summary)
            return dict_recommendation['RECOMMENDATION']

        elif self.timeframe == '5m':
            activ = TA_Handler(symbol=self.active,
                               screener='russia',
                               exchange='MOEX',
                               interval=Interval.INTERVAL_5_MINUTES)

            dict_recommendation = dict(activ.get_analysis().summary)
            return dict_recommendation['RECOMMENDATION']

        elif self.timeframe == '15m':
            activ = TA_Handler(symbol=self.active,
                               screener='russia',
                               exchange='MOEX',
                               interval=Interval.INTERVAL_15_MINUTES)

            dict_recommendation = dict(activ.get_analysis().summary)
            return dict_recommendation['RECOMMENDATION']

        elif self.timeframe == '30m':
            activ = TA_Handler(symbol=self.active,
                               screener='russia',
                               exchange='MOEX',
                               interval=Interval.INTERVAL_30_MINUTES)

            dict_recommendation = dict(activ.get_analysis().summary)
            return dict_recommendation['RECOMMENDATION']

        elif self.timeframe == '1h':
            activ = TA_Handler(symbol=self.active,
                               screener='russia',
                               exchange='MOEX',
                               interval=Interval.INTERVAL_1_HOUR)

            dict_recommendation = dict(activ.get_analysis().summary)
            return dict_recommendation['RECOMMENDATION']

        elif self.timeframe == '2h':
            activ = TA_Handler(symbol=self.active,
                               screener='russia',
                               exchange='MOEX',
                               interval=Interval.INTERVAL_2_HOURS)

            dict_recommendation = dict(activ.get_analysis().summary)
            return dict_recommendation['RECOMMENDATION']

        elif self.timeframe == '4h':
            activ = TA_Handler(symbol=self.active,
                               screener='russia',
                               exchange='MOEX',
                               interval=Interval.INTERVAL_4_HOURS)

            dict_recommendation = dict(activ.get_analysis().summary)
            return dict_recommendation['RECOMMENDATION']

        elif self.timeframe == '1w':
            activ = TA_Handler(symbol=self.active,
                               screener='russia',
                               exchange='MOEX',
                               interval=Interval.INTERVAL_1_WEEK)

            dict_recommendation = dict(activ.get_analysis().summary)
            return dict_recommendation['RECOMMENDATION']


class Crypto(Moex_ta):
    def __init__(self, activ: str, timeframe=None):
        super().__init__(activ, timeframe)

    def time_frame(self) -> str:
        if self.timeframe == '1d' or self.timeframe is None:
            activ = TA_Handler(symbol=self.active,
                               screener='Crypto',
                               exchange='Binance',
                               interval=Interval.INTERVAL_1_DAY
                               )
            activ = dict(activ.get_analysis().summary)
            return activ["RECOMMENDATION"]

        elif self.timeframe == '1m':
            activ = TA_Handler(symbol=self.active,
                               screener='Crypto',
                               exchange='Binance',
                               interval=Interval.INTERVAL_1_MINUTE
                               )
            activ = dict(activ.get_analysis().summary)
            return activ["RECOMMENDATION"]

        elif self.timeframe == '5m':
            activ = TA_Handler(symbol=self.active,
                               screener='Crypto',
                               exchange='Binance',
                               interval=Interval.INTERVAL_5_MINUTES
                               )
            activ = dict(activ.get_analysis().summary)
            return activ["RECOMMENDATION"]

        elif self.timeframe == '15m':
            activ = TA_Handler(symbol=self.active,
                               screener='Crypto',
                               exchange='Binance',
                               interval=Interval.INTERVAL_15_MINUTES
                               )
            activ = dict(activ.get_analysis().summary)
            return activ["RECOMMENDATION"]

        elif self.timeframe == '1h':
            activ = TA_Handler(symbol=self.active,
                               screener='Crypto',
                               exchange='Binance',
                               interval=Interval.INTERVAL_1_HOUR
                               )
            activ = dict(activ.get_analysis().summary)
            return activ["RECOMMENDATION"]

        elif self.timeframe == '4h':
            activ = TA_Handler(symbol=self.active,
                               screener='Crypto',
                               exchange='Binance',
                               interval=Interval.INTERVAL_4_HOURS
                               )
            activ = dict(activ.get_analysis().summary)
            return activ["RECOMMENDATION"]

        elif self.timeframe == '30m':
            activ = TA_Handler(symbol=self.active,
                               screener='Crypto',
                               exchange='Binance',
                               interval=Interval.INTERVAL_30_MINUTES
                               )
            activ = dict(activ.get_analysis().summary)
            return activ["RECOMMENDATION"]

        elif self.timeframe == '2h':
            activ = TA_Handler(symbol=self.active,
                               screener='Crypto',
                               exchange='Binance',
                               interval=Interval.INTERVAL_2_HOURS
                               )
            activ = dict(activ.get_analysis().summary)
            return activ["RECOMMENDATION"]

        elif self.timeframe == '1w':
            activ = TA_Handler(symbol=self.active,
                               screener='Crypto',
                               exchange='Binance',
                               interval=Interval.INTERVAL_1_WEEK
                               )
            activ = dict(activ.get_analysis().summary)
            return activ["RECOMMENDATION"]