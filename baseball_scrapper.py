from pybaseball import statcast
from pybaseball import pitching_stats
import pandas as pd

def scrape_data():
    #Fangraphs

    #data = pitching_stats(2021, 2021)
    #print(data.head())

    #Statcast
    data = statcast(start_dt='2021-06-24', end_dt='2021-06-27')
    print(data.head())

if __name__ == '__main__':
    scrape_data()