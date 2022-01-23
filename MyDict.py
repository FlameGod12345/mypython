import time
data1 = input('Введите день написания: ')
if len(data1) == 0:
    print(' ' * 10)
    print('У тебя ошибка другой мой.')
    print(' ' * 10)
    print('Завершение программы через 2 секунды...')
    time.sleep(2)
    quit()
data2 = input('Введите месяц написания: ')
if len(data2) == 0:
    print(' ' * 10)
    print('У тебя ошибка другой мой.')
    print(' ' * 10)
    print('Завершение программы через 2 секунды...')
    time.sleep(2)
    quit()
data3 = input('Введите год написания: ')
if len(data3) == 0:
    print(' ' * 10)
    print('У тебя ошибка другой мой.')
    print(' ' * 10)
    print('Завершение программы через 2 секунды...')
    time.sleep(2)
    quit()
data = '\n[ ' + data1 + ' / ' + data2 + ' / ' + data3 + ' ]\n'
print(' ' * 10)
list_sorted = input('Введите текст: ')

if len(list_sorted) > 0:
    list_sorted = data + list_sorted[0].upper()+list_sorted[1:]+'\n'
    listik = []
    listik.append(list_sorted)
    a = open('MyDictionary.txt', "a")
    for index in listik:
        a.write(str(index))
        a.close()
else:
    print(' ' * 10)
    print('У тебя ошибка другой мой.')
    print(' ' * 10)
    print('Завершение программы через 2 секунды...')
    time.sleep(2)
    quit()
print(' ' * 10)
b = input('Открыть содержимое файла? [Да - y, нет - n]: ')
print(' ' * 10)
if b == 'y':
    with open('MyDictionary.txt', 'r') as file:
        text = file.read()
        print(text)
else:
    print(' ' * 10)
    print('Завершение программы через 2 секунды...')
    time.sleep(2)
    quit()

killer = input('Закрыть программу? [Да - y, нет - n]: ')
if killer == 'y':
    print(' ' * 10)
    print('Завершение программы через 2 секунды...')
    time.sleep(2)
    quit()
            
