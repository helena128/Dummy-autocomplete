
"""
Прочитать из файла (имя - параметр командной строки)
все слова (разделитель пробел)

Создать "Похожий" словарь который отображает каждое слово из файла
на список всех слов, которые следуют за ним (все варианты).

Список слов может быть в любом порядке и включать повторения.
например "and" ['best", "then", "after", "then", ...] 

Считаем , что пустая строка предшествует всем словам в файле.

С помощью "Похожего" словаря сгенерировать новый текст
похожий на оригинал.
Т.е. напечатать слово - посмотреть какое может быть следующим 
и выбрать случайное.

В качестве теста можно использовать вывод программы как вход.парам. для следующей копии
(для первой вход.парам. - файл)

Файл:
He is not what he should be
He is not what he need to be
But at least he is not what he used to be
  (c) Team Coach


"""

import random
import sys
import random


def mem_dict(filename):
    file = open(filename, "r")
    words = file.read().split()
    #print(words)
    my_dict = {}
    for (idx, w) in enumerate(words):
        if idx == len(words) - 1:
            break
        w_after = words[idx + 1]
        if (w in my_dict):
            saved_w_after = my_dict[w]
        else:
            saved_w_after = []

        # give only unique values
        if (not w_after in saved_w_after):
            saved_w_after.append(w_after)
        my_dict.update({w : saved_w_after})
    return my_dict

def change_phrase(phrase):
    my_dict = mem_dict("1.txt")
    words = phrase.split()
    for idx in range(len(words)):
        if idx == 0:
            continue
        last_word = words[idx - 1]
        change_options = my_dict[last_word]
        chng_idx = random.randint(0, len(change_options) - 1)
        words[idx] = change_options[chng_idx]
    print(words)

def main():
    for i in range (0, 10):
        change_phrase("It is good")



if __name__ == '__main__':
    main()
