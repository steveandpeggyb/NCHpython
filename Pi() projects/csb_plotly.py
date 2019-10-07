
import plotly
import plotly.graph_objs as go
import pandas as pd

# plotly.offline.plot({
#     "data": [go.Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 4])],
#         "layout": go.Layout(title="line chart")
# 	}, auto_open=True)


# Data file is at: 'C:\\Users\\csb003\\Documents\\Python(Git)\\NCHpython\\Pi() projects\\10kVectorPi.csv'

def plotlyDots(d, dest):
    plotly.offline.plot({
        "data": [go.Scatter(x = (d[0]), y=(d[1]))],
        "layout": go.Layout(title='Digits of PI()')
    }, auto_open=True)

filename = 'C:\\Users\\csb003\\Documents\\Python(Git)\\NCHpython\\Pi() projects\\10kVectorPi.csv'
file = open(filename, mode='r')
d=file.read()
file.close()
# plotlyDots(d,'plot')
print(d[1])