status = 'в процессе'
print(f"Текущий статус заметки: {status}")
print('Выберите новый статус заметки:')
print('1. выполнено')
print('2. в процессе')
print('3. отложено')
status = input()
while (status != '1' and status != '2' and
    status != '3' and status != 'выполнено' and
    status != 'в процессе' and status != 'отложено'):
    print('Ввод неверен')
    print('Выберите новый статус заметки:')
    print('1. выполнено')
    print('2. в процессе')
    print('3. отложено')
    status = input()
print(f"Ваш выбор: {status}")
if status == '1':
    status = 'выполнено'
elif status == '2':
    status = 'в процессе'
elif status == '3':
    status = 'отложено'
print(f'Статус заметки успешно обновлён на: "{status}"')
