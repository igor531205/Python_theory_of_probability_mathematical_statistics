# На сколько сигм (средних квадратичных отклонений) отклоняется рост человека,
# равный 190 см, от математического ожидания роста в популяции, в которой
# M(X) = 178 см и D(X) = 25 кв.см?


import numpy


def _z(x: numpy.float64,
       mean: numpy.float64,
       dispersion: numpy.float64) -> numpy.float64:
    '''Функция расчета отклонения Z.
    :param x: Значение.
    :param mean: Среднее значение.
    :param dispersion: Дисперсия.
    :return: Отклонение Z.
    '''
    return (x-mean)/numpy.sqrt(dispersion)


if __name__ == '__main__':

    x = numpy.float64(190.0)
    mean = numpy.float64(178.0)
    dispersion = numpy.float64(25.0)

    print(f'На {_z(x, mean, dispersion)} отклоняется рост человека,',
          'равный 190 см, от математического ожидания роста в популяции,',
          'в которой M(X) = 178 см и D(X) = 25 кв.см')
