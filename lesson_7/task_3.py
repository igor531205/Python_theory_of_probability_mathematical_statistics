# Сравните 1 и 2 е измерения.
# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут:      140, 155, 150, 130, 135


import numpy
from scipy import stats


if __name__ == '__main__':

    x1 = numpy.array([150, 160, 165, 145, 155])
    x2 = numpy.array([140, 155, 150, 130, 135])

    wilcoxon_py = stats.wilcoxon(x1, x2)

    print('Критерий Уилкоксона:',
          f'{wilcoxon_py}', sep='\n')  # Препарат не работает.
