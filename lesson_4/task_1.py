# Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.


import numpy


def _mean(lower_limit: numpy.float64, upper_limit: numpy.float64) -> numpy.float64:
    '''Функция расчета среднего значения равномерного распределения.
    :param lower_limit: Нижняя граница.
    :param upper_limit: Верхняя граница.
    :return: Среднее значение равномерного распределения.
    '''
    return (lower_limit + upper_limit) / 2


def _dispersion(lower_limit: numpy.float64, upper_limit: numpy.float64) -> numpy.float64:
    '''Функция расчета дисперсии равномерного распределения.
    :param lower_limit: Нижняя граница.
    :param upper_limit: Верхняя граница.
    :return: Дисперсия равномерного распределения.
    '''
    return (numpy.power((upper_limit - lower_limit), 2)) / 12


if __name__ == '__main__':

    lower_limit = numpy.float64(200.0)
    upper_limit = numpy.float64(800.0)

    print('Случайная непрерывная величина A имеет равномерное распределение',
          'на промежутке (200, 800].')
    print('Среднее значение равно:',
          _mean(lower_limit, upper_limit))
    print('Дисперсия равна:',
          _dispersion(lower_limit, upper_limit))
