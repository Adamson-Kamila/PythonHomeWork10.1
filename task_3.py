"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
words = ["attribute", "класс", "функция", "type"]
for word in words:
    try:
        b_word = bytes(word, "utf-8")
        print(f"{word}: {b_word}")
    except:
        print(f"{word} невозможно записать в байтовом формате с помощью маркировки b''")