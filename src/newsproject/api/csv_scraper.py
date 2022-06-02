import pandas as pd
import os
from os.path import isfile, join

def get_csv_articles():
    list_files = [f for f in os.listdir('./api/data/') if isfile(join('./api/data/', f))]

    urls = []

    for file in list_files:
        df = pd.read_csv(f'./api/data/{file}')
        urls.extend(df['Link'].tolist())
    
    return urls