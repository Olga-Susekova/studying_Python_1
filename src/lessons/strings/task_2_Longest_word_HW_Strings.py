#Задание
#Найти самое длинное слово в введенном предложении

a = input('enter your sentence')
#a="this is maximum word"

max_symb = 0
longest_word = ""

# вычленяем слово,
# ставим его в переменную b,
# сравниваем длину b с переменной max_word(изначально она =0 по нашим условиям)
# если длина b больше max_word, записываем ее в  max_word (переменную) для дальнейших сравнений
# и записываем в longest_word слово из переменной b для вывода результата на экран(или др.операций с объектом)
# выводим на экран переменную longest_word, в которой записано слово из переменной b, у которого длина > max_word из всего цикла сравнений по словам.

every_word = a.split()  # разбиваем предложение из переменной а на слова
for b in every_word:  # здесь подставляется каждое слово из предложения в переменную b
    if len(b) > max_symb: # если длина симв слова b > max_symb(сравнив с предыдущ макс словом) (допутим B=9,9>0)
        max_symb = len(b) # тогда приравниваем переменной max_symb кол-во символов от переменной b (max_symb=9) для дальнейших сравнений
        longest_word = b #и записываем в longest_word слово из переменной b для вывода результата на экран(или др.операций с объектом)
print('the longest word is', longest_word)
print('the number of characters is', max_symb)

