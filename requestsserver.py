import pandas as pd
import requests
from matplotlib import pyplot as plt
from random import choice
import string


class Stoke_Market_chart:
    def __init__(self, active: str, initial_time: str, end_time: str):
        self.active = active
        self.initial_time = initial_time
        self.end_time = end_time

    def chart(self) -> str:
        get_request = requests.get(
            f'http://iss.moex.com/iss/engines/stock/markets/shares/securities/{self.active}/candles.json?from={self.initial_time}&till={self.end_time}&interval=24').json()
        data = []
        for i in get_request['candles']['data']:
            data.append({j: i[number] for number, j in enumerate(get_request['candles']['columns'])})
        frame = pd.DataFrame(data)
        random_symbol = [choice([element for element in string.ascii_letters]) for _ in range(5)]
        plt.plot(list(frame['close']))
        name_file = f'{self.active}{self.initial_time}{self.end_time}{random_symbol}.png'
        plt.savefig(name_file)
        plt.close()
        return name_file