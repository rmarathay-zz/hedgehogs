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
    ax = plt.subplot(1, 1, 1)
    ax.scatter(dates, cl)
    ax.plot(dates, cl, "or")
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