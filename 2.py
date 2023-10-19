def task(num):
    count = 0
    res = {}
    while count < num:
        name, char = input('Введи имя и знак зодиака через запятую: ').split(',')
        res[name] = char
        count += 1
    return res


print(task(2))
