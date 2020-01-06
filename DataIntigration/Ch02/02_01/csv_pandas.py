"""Load & converting data from CSV using Pandas"""
import pandas as pd
FilePath = 'C:/Users/csb003/Documents/NCHpython/DataIntigration/Ch02/02_01/taxi.csv.bz2'

time_cols = ['tpep_dropoff_datetime', 'tpep_pickup_datetime']


def load_df(file_name):
    return pd.read_csv(FilePath, parse_dates=time_cols)


print(load_df(FilePath).head())


def iter_df(file_name):
    yield from pd.read_csv(
        FilePath, parse_dates=time_cols, chunksize=100)


for i, df in enumerate(iter_df(FilePath)):
    if i > 10:
        break
    print(len(df))
