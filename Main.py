import os
import quandl
import time
import csv
from FallingMassiveCompany import strategy


apiKey = '9Wf92g7DtdVbKudQJRvR'
link = 'https://www.quandl.com/api/v3/databases'
quandl.ApiConfig.api_key = apiKey

with open('EOD_metadata.csv', newline='') as csvf:
    meta = list(csv.reader(csvf))


with open('NASDAQ_20190527_20190827.csv', newline='') as csvf:
    data = list(csv.reader(csvf))

pool = []

symb = None
ind = 1
start = 1
stocks_count = 0
while ind < len(data):
    if data[ind][0] != symb:
        if strategy(data[start:ind]):
            pool.append(symb)

        symb = data[ind][0]
        start = ind
        stocks_count += 1
    ind += 1

print(stocks_count, 'stocks analyzed')
print("qualified:")
print(pool)
