from tradingview_ta import TA_Handler, Interval


class Moex_ta:
    def __init__(self, active: str, timeframe=None):
        self.active = active
        self.timeframe = timeframe
        self.interpreter = {'SELL': 'Продавать', 'BUY': 'Покупать', 'NEUTRAL': 'Нейтрально'}

    def technical_analysis(self):
        technical_analysis_ = self.time_frame()
        return self.interpreter[technical_analysis_]

    def time_frame(self):
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


# class Crypto(Moex_ta):
#     def __init__(self, activ, timeframe):
#         super().__init__(activ, timeframe)

