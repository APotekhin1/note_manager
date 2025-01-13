status = 'в процессе' # текущий статус
print(f"Текущий статус заметки: {status}")
# список возможных статусов для ввода
print('Выберите новый статус заметки:')
print('1. выполнено')
print('2. в процессе')
print('3. отложено')
status = input()
# цикл определяет верность ввода статуса
while status not in ['1', '2', '3', 'выполнено', 'в процессе', 'отложено']:
    print('Ввод неверен')
    print('Выберите новый статус заметки:')
    print('1. выполнено')
    print('2. в процессе')
    print('3. отложено')
    status = input()
print(f"Ваш выбор: {status}")
# если статус был введен цифрой, заменим его на ввод строкой
if status == '1':
    status = 'выполнено'
elif status == '2':
    status = 'в процессе'
elif status == '3':
    status = 'отложено'
# вывод нового статуса зметки
print(f'Статус заметки успешно обновлён на: "{status}"')
