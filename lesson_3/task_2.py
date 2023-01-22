# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике -
# 12 мячей, из которых 5 белых. Из первого ящика вытаскивают случайным образом
# два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?


from math import comb

if __name__ == '__main__':

    def _func1(num): return comb(5, num) * comb(3, 2-num) / comb(8, 2)
    p1 = [_func1(num) for num in range(3)]
    # print(f'Проверка результата: {sum(p1):.1f}')

    def _func2(num): return comb(5, num) * comb(7, 4-num) / comb(12, 4)
    p2 = [_func2(num) for num in range(5)]
    # print(f'Проверка результата: {sum(p2):.1f}')

    p = p1[0]*p2[3] + p1[1]*p2[2] + p1[2]*p2[1]
    print('Вероятность, что три мяча белые равна', f'{p:.5f}')
