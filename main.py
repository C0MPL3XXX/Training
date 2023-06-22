import requests
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

url = 'https://www.alphavantage.co/support/query?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&symbol=SPY&apikey=KJHKP6CLUF0BQ40A'

r = requests.get(url)

data = r.json()
u_data = data['Time Series (Daily)']

# This function shows individual days returns, and it also shows the return for the specified month, it can also compare
# months.
def monthly():

    repeat_m = input('How many months do you wish to compare?')

    for o in range(0, int(repeat_m)):
        t_returns = []
        month = input('What month do you wish to see the returns on(1-12)?')
        year = input('What year is this month in(2000-2023)?')
        print("The Return of ", year, "/", month, ":", "\n")
        for i in u_data:
            m = int(str(i[5]) + str(i[6]))
            y = int(str(i[0]) + str(i[1]) + str(i[2]) + str(i[3]))
            if m == int(month) and y == int(year):
                day = int(str(i[8]) + str(i[9]))
                m_data = u_data[i]
                returns_d = float(m_data['1. open']) - float(m_data['4. close'])
                print("Day", day, ":", "%.4f" % returns_d, "\n")
                t_returns.append(returns_d)

        print("Return of the month:", "%.4f" % sum(t_returns), "\n")

# This function uses lists, temporary variables, and loops to calculate the individual months return, as well as the
# total in the year, it can also print more than one year, so it is possible to compare.
def yearly():
    temp = 0
    temporary = []
    returns_y = []
    repeat_y = input('How many years do you wish to compare?')

    for o in range(0, int(repeat_y)):
        year = input('What year(1999-2023)?')

        for i in u_data:
            y = int(str(i[0]) + str(i[1]) + str(i[2]) + str(i[3]))

            if y == int(year):
                month = int(str(i[5]) + str(i[6]))
                m_data = u_data[i]
                returns_d = float(m_data['1. open']) - float(m_data['4. close'])
                temporary.append(returns_d)

                if month != temp:
                    temp = month
                    returns_y.append(sum(temporary))
                    print("Return of the", month, "month:", "%.4f" % sum(temporary), "\n")

        print("Return in", year, ":", "%.4f" % sum(returns_y), "\n")


# This was my first loop to experiment with the data, this shows every single days return from 1999 to 2023.
def full_data_loop():

    for m in u_data:
        d_data = u_data[m]
        returns_d = float(d_data['1. open']) - float(d_data['4. close'])
        a_returns_d = float(d_data['1. open']) - float(d_data['5. adjusted close'])
        print("Daily Return of " + m + ":", "%.4f" % returns_d)
        print("Daily Adjusted Return of " + m + ":", "%.4f" % a_returns_d, "\n")



function = input("Do you wish to see Yearly(1) or Monthly(2) returns? For full (daily) data enter 3.")

if int(function) == 1:
    yearly()
if int(function) == 2:
    monthly()
if int(function) == 3:
    full_data_loop()

