# Задание
# Посчитать количество
# строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы
text = input('enter your data')
a_lower = 0
a_upper = 0
alp_lat = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in text:
    if i in alp_lat:
        if i.islower():
            a_lower += 1
        elif i.isupper():
            a_upper += 1
print('The number of upper letters is', a_upper)
print('The number of lower letters is', a_lower)