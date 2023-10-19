def replace(my_list):
    for i in range(len(my_list)):
        my_list[i] = my_list[i].replace('ё', 'е')
        my_list[i] = my_list[i].replace('Ё', 'Е')


# Здесь вводить в задание надо только функции
# Без функции range тут очень неудобно решать, я думаю вы её проходили в циклах фор

a = ['qw', 'еоё', 'Ёпуеё']
replace(a)
print(a)
