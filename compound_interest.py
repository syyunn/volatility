import math

import matplotlib.pyplot as plt


def get_compounded_price(t, initial_price, interest_rate):
    upper = interest_rate * t
    print("upper: {}".format(upper))
    exponential = math.exp(upper)
    print("exponential: {}".format(exponential))
    return initial_price * exponential


if __name__ == "__main__":
    prices = []
    times = []

    interest_rate = 0.01
    initial_price = 1000000
    for t in range(1, 1000):
        price = get_compounded_price(t,
                                     initial_price,
                                     interest_rate)
        times.append(t)
        prices.append(price)

    plt.plot(times, prices)
    plt.show()
    pass
