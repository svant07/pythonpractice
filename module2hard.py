


def get_random_num():
    numbers = list(range(3, 21))
    random_num = int(input('Введите число от 3 до 20: '))
    return random_num


n = get_random_num()

first = list(range(1, n))
second = list(range(1, n))
passw = []
result = ''
for i in first:
    for j in second:
        if i >= j:
            continue
        else:
            a = n % (i + j)
            if a == 0:
                passw.append(i)
                passw.append(j)
                result = result + str(i) + str(j)

print('Пароль: ', result)

