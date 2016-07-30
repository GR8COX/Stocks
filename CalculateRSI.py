import pandas
import pandas.io.data
import matplotlib.pyplot as plt


def calculateRSI(data: object, window: object) -> object:
    # Window length for moving average
    window_length = window

    # Get data

    # Get just the close
    close = data['Close']
    # Get the difference in price from previous step
    delta = close.diff()
    # Get rid of the first row, which is NaN since it did not have a previous
    # row to calculate the differences
    delta = delta[1:]

    # Make the positive gains (up) and negative gains (down) Series
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    # Calculate the EWMA
    roll_up1 = pandas.stats.moments.ewma(up, window_length)
    roll_down1 = pandas.stats.moments.ewma(down.abs(), window_length)

    # Calculate the RSI based on EWMA
    RS1 = roll_up1 / roll_down1
    RSI1 = 100.0 - (100.0 / (1.0 + RS1))

    # Calculate the SMA
    roll_up2 = pandas.rolling_mean(up, window_length)
    roll_down2 = pandas.rolling_mean(down.abs(), window_length)

    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))

    # Compare graphically
    plt.figure()
    RSI1.plot()
    RSI2.plot()
    plt.legend(['RSI via EWMA', 'RSI via SMA'])
    plt.show()
    return {RSI1[-1], RSI2[-1]}