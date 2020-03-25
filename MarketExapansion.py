""" Anish’s Market Expansion strategy (For Longs)

data row
[Symbol,Date,Open,High,Low,Close,Volume]

Anish’s Market Expansion strategy (For Longs)
The strategy uses daily price data, daily volume and the ADX Indicator (average directional indicator).
It goes as follows-

1.  	If the stock has a daily average (last 20 trading days) volume of at least 200K, keep it in the pool.
If not, discard it.

2.  	If also, the stock reached a new 65 day high at any time today, keep it in the pool. If not, discard it.
It has to be a brand new high (absolute maximum in 65 day period).

3.  	If also, the price range (high – low) of the day is greater than the range of all of the previous nine
trading days, keep the stock in the pool. If not, discard it.

4.  	If also, the price closes in the upper 25% of the price range of the day, keep it in the pool. If not,
discard it. E.g. Low is $1, high is $1.20 and it closes at $1.10 then it is not in the upper 25%. If it closes
at $1.15 or greater then it is.

5.  	Lastly, the ADX indicator (explained below), if the relevant stock market index (e.g. TSX for Canadian stocks)
closed at a greater value than it closed five days ago then the stock must also have DI+ > DI- with the ADX at a value
greater than 30. If the ADX value has fallen compared to the previous day or is below 30 then discard the stock.

6.  	Buy into the stock immediately as the market opens the next day. I usually try to buy into it at one tick below
its opening price. E.g. Open at $1, I try to buy it at $0.99 if possible.


"""
SYMBOL = 0
DATE = 1
OPEN = 2
HIGH = 3
LOW = 4
CLOSE = 5
VOLUME = 6


def strategy(data):
    """ evaluate if the stock of given data should be kept in the pool """
    if len(data) < 65:  # days of data needed
        return False

    # make float
    for i in range(len(data)):
        for j in range(2, 7):
            data[i][j] = float(data[i][j])
    # rule 1
    if sum(day[VOLUME] for day in data[-20:]) / 20 < 200000:
        return False

    # rule 2
    if any(data[-1][HIGH] <= day[HIGH] for day in data[-65:-1]):
        return False

    # rule 3
    prg = data[-1][HIGH] - data[-1][LOW]
    for day in data[-9: -1]:
        hrg = day[HIGH] - day[LOW]
        if hrg > prg:
            return False

    # rule 4
    if data[-1][CLOSE] <= data[-1][LOW] + 0.75 * prg:
        return False

    # rule 5




    return True


