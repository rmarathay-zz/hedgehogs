import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects


#params: dates Datetime object list representing stock dates
#        cl List of floats representing closing values for each date
# produces a graph of the closing values for each day over 3 months.
def plotClose(dates, cl):
    plt.figure(1)
    plt.plot(dates, cl, linewidth=2, color='red',
             path_effects=[path_effects.SimpleLineShadow(),
                           path_effects.Normal(offset=(0.0,5.0))])

    plt.xlabel("Date (Month)")
    plt.ylabel("Value ($)")
    plt.title("Daily Closing Values")
    plt.show()

#params: dates Datetime object list representing stock dates
#        op List of floats representing open values for each date
# produces a graph of the open values for each day over 3 months.
def plotOpen(dates, op):
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

#params: cl Closing prices for the last 90 days of a stock
#returns simple moving average of the closing values
def calculateSMA(cl):
    N = 10
    cumsum, moving_aves = [0], []

    for i, x in enumerate(cl, 1):
        cumsum.append(cumsum[i - 1] + x)
        if i >= N:
            moving_ave = (cumsum[i] - cumsum[i - N]) / N
            # can do stuff with moving_ave here
            moving_aves.append(moving_ave)
    return moving_ave
    