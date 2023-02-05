# Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
# Проверить данную гипотезу, если известно, что размеры изделий подчинены
# нормальному закону распределения. Объем выборки 10, уровень статистической
# значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34


import numpy
from scipy import stats


if __name__ == '__main__':

    a = numpy.array([2.51, 2.35, 2.74, 2.56, 2.40,
                    2.36, 2.65, 2.7, 2.67, 2.34])

    x_1 = a.mean()
    std_x = a.std(ddof=1)
    n = a.size
    m = 2.5

    t1 = numpy.round((x_1 - m) / std_x * numpy.sqrt(n), 3)

    # По таблице Критерий t = 1.833 (для 0.95 и 9 степеней свободы).
    t = 1.833

    print(f't1 = {t1}',
          f't = {t}',
          f't1 < t -> Гипотеза Н0 верна',
          sep='\n')
