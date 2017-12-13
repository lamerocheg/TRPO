import random

import matplotlib.pyplot as plt
import numpy as np


def generate_list():
    return list([random.normalvariate(mu=1, sigma=1) for i in range(100)])


def calculate_ranges(l):
    return list([l[i] - l[i - 1] for i in range(1, len(l))])


if __name__ == '__main__':
    random_list = generate_list()
    print("случайная последовательность: {}".format(random_list))

    sorted_list = sorted(random_list)
    print("Отсортированный список: {}".format(sorted_list))

    ranges = calculate_ranges(sorted_list)
    print("Значения расстояний между элементами: {}".format(ranges))

    print("среднее значение : {}".format(sum(ranges) / len(ranges)))

    print("Дисперсия : {}".format(np.var(ranges)))

    plt.hist(ranges)
    plt.title("расстояния между результатами")
    plt.xlabel("значение")
    plt.ylabel("расстояние")
    plt.show()
