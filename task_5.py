"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

# Функция для выполнения пинга
def ping(address):
    result = subprocess.run(['ping', 'www.youtube.com'], capture_output=True)
    encoding = chardet.detect(result.stdout)['encoding']
    return result.stdout.decode(encoding)

# Выполнение пинга и вывод результата в консоль
print(ping('yandex.ru'))
print(ping('youtube.com'))