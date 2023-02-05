# Даны 3 группы учеников плавания.
# В 1 группе время на дистанцию 50 м составляют:
# 56, 60, 62, 55, 71, 67, 59, 58, 64, 67
# Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
# Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54
# Есть ли различия между группами?


import numpy
from scipy import stats


if __name__ == '__main__':

    x1 = numpy.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
    x2 = numpy.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
    x3 = numpy.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

    kruskal_py = stats.kruskal(x1, x2, x3)

    print('Критерий Крускала – Уоллиса:',
          f'{kruskal_py}', sep='\n')  # Группы равны