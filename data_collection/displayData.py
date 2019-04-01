import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects


def plotClose(dates, cl):
    """
    
    produces a graph of the closing values for each day over 3 months.

    Arguments:
        dates: Datetime object list representing stock dates
#       cl: List of floats representing closing values for each date

    """
    plt.figure(1)
    plt.plot(dates, cl, linewidth=2, color='red',
             path_effects=[path_effects.SimpleLineShadow(),
                           path_effects.Normal(offset=(0.0,5.0))])
    ax = plt.subplot(1, 1, 1)
    ax.scatter(dates, cl)
    ax.plot(dates, cl, "or")
    plt.xlabel("Date (Month)")
    plt.ylabel("Value ($)")
    plt.title("Daily Closing Values")
    plt.show()

def plotOpen(dates, op):
    """

    produces a graph of the open values for each day over 3 months.

    Arguments:
        dates: Datetime object list representing stock dates
        op: List of floats representing open values for each date


    """
    plt.plot(dates, op, linewidth=2, color='red',
             path_effects=[path_effects.SimpleLineShadow(),
                           path_effects.Normal(offset=(0.0,5.0))])
    ax = plt.subplot(1, 1, 1)
    ax.scatter(dates, op)
    ax.plot(dates, op, "or")
    plt.xlabel("Date (Month)")
    plt.ylabel("Value ($)")
    plt.title("Daily Open Values")
    plt.show()

def calculateSMA(cl):
    """
    
    calculates simple moving average

    Arguments:
        cl: Closing prices for the last 90 days of a stock

    Returns:
        simple moving average of the closing values

    """
    N = 10
    cumsum, moving_aves = [0], []

    for i, x in enumerate(cl, 1):
        cumsum.append(cumsum[i - 1] + x)
        if i >= N:
            moving_ave = (cumsum[i] - cumsum[i - N]) / N
            # can do stuff with moving_ave here
            moving_aves.append(moving_ave)
    return moving_ave
    