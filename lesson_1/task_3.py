from math import comb


if __name__ == '__main__':
    '''
    В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий 
    случайным образом извлекает 3 детали. Какова вероятность 
    того, что все извлеченные детали окрашены?
    '''
    m = comb(9, 3)
    n = comb(15, 3)
    p = m / n
    print(f'Вероятность p = {p:.4f}')
