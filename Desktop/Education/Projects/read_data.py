import pandas as pd

def read_data(link):
    data_set = pd.read_csv(link, header=0)
    return data_set

