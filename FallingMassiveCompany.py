""" Jack’s Falling Massive company

data row
[Symbol,Date,Open,High,Low,Close,Volume]

This strategy aims to find companies that reached a low in a certain period,
but trading at overall high volume and generally good to hold.

find overreacted under valued stocks
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
    if len(data) < 55:  # days of data needed
        return False

    # make float
    for i in range(len(data)):
        for j in range(2, 7):
            data[i][j] = float(data[i][j])
    # rule 1
    if sum(day[VOLUME] for day in data[-20:]) / 20 < 200000:
        return False

    # rule 2
    if any(data[-1][LOW] >= day[LOW] for day in data[-10:-1]):
        return False

    # rule 3
    prg = data[-1][HIGH] - data[-1][LOW]
    for day in data[-9: -1]:
        hrg = day[HIGH] - day[LOW]
        if hrg > prg:
            return False

    # rule 4
    if data[-1][CLOSE] >= data[-1][LOW] + 0.70 * prg:
        return False

    # rule 5
    if data[-1][CLOSE] >= 0.90 * data[0][CLOSE]:
        return False

    # rule 6
    if data[-1][CLOSE] < 2:
        return False



    return True


