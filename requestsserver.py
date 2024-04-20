import pandas as pd
import requests
from matplotlib import pyplot as plt
from random import choice
import string


class Stoсke_Market_chart:
    def __init__(self, active: str, initial_time: str, end_time: str):
        self.active = active
        self.initial_time = initial_time
        self.end_time = end_time

    def chart(self) -> str:
        text = 'iss.moex.com/iss/engines/stock/markets/shares/securities'
        text_2 = 'candles.json?from'
        get_request = requests.get(
            f'http://{text}/{self.active}/{text_2}={self.initial_time}&till={self.end_time}&interval=24').json()
        data = []
        for element_dict in get_request['candles']['data']:
            data.append({j: element_dict[number] for number, j in enumerate(get_request['candles']['columns'])})
        frame = pd.DataFrame(data)
        random_symbol = [choice([element for element in string.ascii_letters]) for _ in range(5)]
        plt.plot(list(frame['close']))
        name_file = f'{self.active}{self.initial_time}{self.end_time}{random_symbol}.png'
        plt.savefig(name_file)
        plt.close()
        return name_file