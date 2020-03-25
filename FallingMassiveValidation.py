import csv
from FallingMassiveCompany import strategy

SYMBOL = 0
DATE = 1
OPEN = 2
HIGH = 3
LOW = 4
CLOSE = 5
VOLUME = 6


with open('NASDAQ_20190527_20190827.csv', newline='') as csvf:
    data = list(csv.reader(csvf))

pool = []

symb = None
ind = 1
start = 1
stocks_count = 0
uppp = 0  # 10% +
upp = 0  # 5% +
up = 0  # +
down = 0  # 10% -
downn = 0   # 5% -
downnn = 0  # -

for i in range(1, len(data)):
    for j in range(2, 7):
        data[i][j] = float(data[i][j])

while ind < len(data):
    if data[ind][0] != symb:
        if strategy(data[start:ind - 5]):
            pool.append(symb)
            if 1.1 * data[ind - 5][CLOSE] < data[ind][CLOSE]:
                uppp += 1
            elif 1.05 * data[ind - 5][CLOSE] < data[ind][CLOSE]:
                upp += 1
            elif data[ind - 5][CLOSE] < data[ind][CLOSE]:
                up += 1
            elif 0.9 * data[ind - 5][CLOSE] > data[ind][CLOSE]:
                downnn += 1
            elif 0.95 * data[ind - 5][CLOSE] > data[ind][CLOSE]:
                downn += 1
            elif data[ind - 5][CLOSE] > data[ind][CLOSE]:
                down += 1

        symb = data[ind][0]
        start = ind
        stocks_count += 1
    ind += 1

print(stocks_count, 'stocks analyzed')
print("qualified:")
print(pool)
print("uppp count: ", uppp)
print("upp count: ", upp)
print("up count: ", up)
print("down count: ", down)
print("downn count: ", downn)
print("downnn count: ", downnn)
print("total = ", len(pool))
print("up / down: ", (up + upp + uppp) / (down + downn + downnn))
