def to_dollars(num):
    return num // 75


def to_euros(num):
    return num // 85


def new_converter(num):
    return to_dollars(num), to_euros(num)


# Здесь вводить в задание надо только функции

print(new_converter(10000))
