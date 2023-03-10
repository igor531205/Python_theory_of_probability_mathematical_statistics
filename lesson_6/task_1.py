# Известно, что генеральная совокупность распределена нормально со средним
# квадратическим отклонением, равным 16. Найти доверительный интервал для
# оценки математического ожидания a с надежностью 0.95, если выборочная
# средняя M = 80, а объем выборки n = 256.


import numpy


if __name__ == '__main__':

    M = 80
    n = 256
    std = 16
    Z = 1.96  # для надежности 0.95 -> 0,05/2 -> 0,025

    L = numpy.round(M - Z * std / numpy.sqrt(n), 2)
    U = numpy.round(M + Z * std / numpy.sqrt(n), 2)

    print(f'Доверительный интервал [ {L} ; {U} ]')
