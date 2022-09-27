# Вводится строка.
# Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef"
a = input("enter your data")
a_scr = ""
a = a.replace(' ', '')
for i in a:
    if not i in a_scr:
        a_scr += i
print(a_scr)
