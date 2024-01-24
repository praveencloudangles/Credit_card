import pandas as pd

def data_loading():
    df = pd.read_csv("CC GENERAL.csv")

    return df

data_loading()