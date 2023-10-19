def to_dollars(num):
    return num // 75


def convert_to_dollars(nums):
    number = []
    for num in nums:
        number.append(str(to_dollars(num)))
    return ' '.join(number)


# Здесь вводить в задание надо только функции

print(convert_to_dollars([150, 1000]))
