import string

inpt = ("На что нужен экипаж в городе, где нет и четырех тысяч жителей? Долой папу! (Дела с Римом запутывались.) "
        "Я за Цезаря, и только за Цезаря. И т.д. и т.д.")

for char in string.punctuation:
    inpt = inpt.replace(char, '').upper()

print(inpt)
