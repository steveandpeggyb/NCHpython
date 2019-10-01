import pandas as pd
import itertools as i

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return i.zip_longest(*args, fillvalue=fillvalue)

def Build():
    zero_to_Nintynine = pd.Series(range(0,100))
    series = list(grouper(10, zero_to_Nintynine))
    series_len = len(series)
    # print(series_len)
    # print(list(series))
    for i in range(10):
        print(series[i])
    
if __name__ == '__main__':
    Build()