previous = 0
res = True
while True:
    num = int(input('Траты: '))
    if num < 0:
        break
    if previous > num:
        res = False
    previous = num

print(res)
