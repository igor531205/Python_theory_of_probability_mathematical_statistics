# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности
# среднего роста родителей и детей.


import numpy
from scipy import stats


if __name__ == '__main__':

    a = numpy.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
    b = numpy.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])

    n1 = a.size
    n2 = b.size

    x_1 = a.mean()
    x_2 = b.mean()
    delta = x_1 - x_2

    D1 = a.var(ddof=1)
    D2 = b.var(ddof=1)
    D = (D1 + D2) / 2

    SE = numpy.sqrt(D/n1 + D/n2)

    t1 = stats.t.ppf(0.975, (n1 - 1 + n2 - 1))

    L = numpy.round(delta - t1 * SE, 2)
    U = numpy.round(delta + t1 * SE, 2)

    print(f'Доверительный интервал [ {L} ; {U} ]')
