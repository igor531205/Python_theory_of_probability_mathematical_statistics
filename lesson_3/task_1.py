'''
Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25,
65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. Посчитать
среднее арифметическое, среднее квадратичное отклонение, смещенную и
несмещенную оценки дисперсий для данной выборки.
'''


import numpy


def _root_mean_square(numbers: numpy.array) -> float:
    '''Функция расчета суммы квадратов отклонений.
    :param array: Список чисел.
    :return: Сумма квадратов отклонений.
    '''
    mean_numbers = mean(numbers)

    return float(numpy.sum(numpy.power(numbers - mean_numbers, 2)))


def mean(numbers: numpy.array) -> float:
    '''Функция расчета среднего арифметического.
    :param array: Список чисел.
    :return: Среднее арифметическое.
    '''
    return float(numbers.sum() / numbers.size) if numbers.size else 0.0


def standard_deviation(numbers: list) -> float:
    '''Функция расчета среднего квадратичного отклонения.
    :param array: Список чисел.
    :return: Среднее квадратичное отклонение.
    '''
    root_mean_square = _root_mean_square(numbers)

    return float(numpy.sqrt(root_mean_square / salary_array.size))


def shifted_variance(numbers: numpy.array) -> float:
    '''Функция расчета смещенной дисперсии.
    :param array: Список чисел.
    :return: Смещенная дисперсия.
    '''
    root_mean_square = _root_mean_square(numbers)

    return float(numpy.sqrt(root_mean_square / salary_array.size))


def unbiased_variance(numbers: numpy.array) -> float:
    '''Функция расчета несмещенной дисперсии.
    :param numbers: Список чисел.    
    :return: Несмещенная дисперсия.
    '''
    root_mean_square = _root_mean_square(numbers)

    return float(numpy.sqrt(root_mean_square / (salary_array.size - 1)))


if __name__ == '__main__':

    salary_array = numpy.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30,
                                24, 57, 55, 70, 75, 65, 84, 90, 150])
    salary_array.sort()

    print('Зарплаты из выборки выпускников:',
          *salary_array)

    print('Среднее арифметическое:',
          f'{mean(salary_array):.1f}')
    # print(f'Проверка результата: {salary_array.mean():.1f}')

    print('Среднее квадратичное отклонение:',
          f'{standard_deviation(salary_array):.1f}')
    # print(f'Проверка результата: {salary_array.std():.1f}')

    print('Смещенная дисперсия:',
          f'{shifted_variance(salary_array):.1f}')
    # print(f'Проверка результата: {salary_array.std():.1f}')

    print('Несмещенная дисперсия:',
          f'{unbiased_variance(salary_array):.1f}')
    # print(f'Проверка результата: {salary_array.std(ddof=1):.1f}')
