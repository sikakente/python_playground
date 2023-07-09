from functools import partial


def power(a, b):
    return a ** b


power_of_5 = partial(power, b=5)

if __name__ == '__main__':
    print(list(map(power_of_5, list(range(10)))))
