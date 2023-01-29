# О случайной непрерывной равномерно распределенной величине B известно,
# что ее дисперсия равна 0.2. Можно ли найти правую границу величины B
# и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.


import numpy


def _mean(lower_limit: numpy.float64, upper_limit: numpy.float64) -> numpy.float64:
    '''Функция расчета среднего значения равномерного распределения.
    :param lower_limit: Нижняя граница.
    :param upper_limit: Верхняя граница.
    :return: Среднее значение равномерного распределения.
    '''
    return (lower_limit + upper_limit) / 2


def _upper_limit(lower_limit: numpy.float64, dispersion: numpy.float64) -> numpy.float64:
    '''Функция расчета верхней границы равномерного распределения.
    :param lower_limit: Нижняя граница.
    :param upper_limit: Дисперсия.
    :return: Верхняя граница равномерного распределения.
    '''
    return numpy.sqrt(dispersion * 12) + lower_limit


if __name__ == '__main__':

    dispersion = numpy.float64(0.2)
    lower_limit = numpy.float64(0.5)

    upper_limit = _upper_limit(lower_limit, dispersion)

    print('Левая граница случайной непрерывной равномерно распределенной',
          'величины B равна 0.5, \nдисперсия равна 0.2.')
    print('Правая граница равна:',
          upper_limit)
    print('Среднее значение равно:',
          _mean(lower_limit, upper_limit))
