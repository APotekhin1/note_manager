from datetime import date, datetime # включаем библиотеки datetime для работы с датами

# файл add_titles_loop.py
print()
print('Файл add_titles_loop.py \n')
list = [] # задаем начальное значение списку заголовков
title = input('Введите заголовок (или оставьте пустым для завершения): ') # ввод первого значения
while title != '' and title != 'стоп': # если не пустое и не спецкоманда, то идем в цикл
    if title not in list:  # проверка на уникальность заголовков, чтобы избежать повторов
        list.append(title)
    title = input('Введите заголовок (или оставьте пустым для завершения): ') # ввод следующего заголовка
# вывод списка заголовков
for i in range(len(list)):
    print('-', list[i])

# файл update_status.py
print()
print('Файл update_status.py \n')
status = 'в процессе'  # текущий статус
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

# файл check_deadline.py
print()
print('Файл check_deadline.py \n')
today_date = date.today() # узнаем сегодняшнюю дату
print("Текущая дата: {}-{}-{}".format(today_date.day, today_date.month, today_date.year))
while True: # цикл для определения корректной даты ввода
    issue_date = input("Введите дату дедлайна (в формате 'день-месяц-год'): ")
    try:
        issue_date = datetime.strptime(issue_date, '%d-%m-%Y')
        break
    except ValueError as e:
        print(e)
# определение количества дней между сегодняшней и введенной латами
date1 = datetime(today_date.year, today_date.month, today_date.day)
date2 = datetime(issue_date.year, issue_date.month, issue_date.day)
delta = (date2 - date1).days
# определение корректного окончания слова в зависимости от количества дней
day = 'дней'
if abs(delta) % 10 == 1:
    day = 'день'
elif 1 < abs(delta) % 10 < 5:
    day = 'дня'
# вывод информации о дедлайне
if delta < 0:
    print(f"Внимание! Дедлайн истёк {abs(delta)} {day} назад") # Вывод предупреждения об истечении срока дедлайна
elif delta > 0:
    print(f"До дедлайна осталось {delta} {day}")  # Вывод предупреждения о дедлайне
else:
    print('Дедлайн сегодня!')

# файл multiple_notes.py.py
print()
print('Файл multiple_notes.py.py \n')
answer = input('Добро пожаловать в "Менеджер заметок"! Хотите добавить новую заметку? ')
notes = [] # начальное значение вводимого списка заметок
while answer != 'стоп' and answer != 'нет':
    # ввод текущего элемента
    name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    created_date = datetime.now().strftime("%d-%m-%Y")
    while True:  # цикл для определения корректной даты ввода
        issue_date = input("Введите дедлайн (день-месяц-год): ")
        try:
            # Пробуем преобразовать введённую дату
            datetime.strptime(issue_date, "%d-%m-%Y")
            break
        except ValueError as e:
            print(e)
    # создание элемента списка в виде словаря
    note = {
        "Имя": name,
        "Заголовок": title,
        "Описание": content,
        "Статус": status,
        "Дата создания": created_date,
        "Дедлайн": issue_date
    }
    notes.append(note)
    answer = input('Хотите добавить еще заметку? ')
# ввывод всех элементов списка, вывод дат в виде ДД-ММ-ГГГГ
print("\nСписок заметок:")
for i, note in enumerate(notes, start=1):
    print(f"\n{i}. Имя: {note['Имя']}\n   Заголовок: {note['Заголовок']}\n"
          f"   Описание: {note['Описание']}\n   Статус: {note['Статус']}\n"
          f"   Дата создания: {note['Дата создания']}\n   Дедлайн: {note['Дедлайн']}")

# Файл delete_note.py
print()
print('Файл delete_note.py \n')
# Изначальный список заметок
notes = [
    {"Имя": "Алексей", "Заголовок": "Список покупок", "Описание": "Купить продукты на неделю"},
    {"Имя": "Мария", "Заголовок": "Учеба", "Описание": "Подготовиться к экзамену"},
    {"Имя": "Василий", "Заголовок": "Список покупок", "Описание": "Хлеб, молоко, сыр"},
    {"Имя": "Алексей", "Заголовок": "Встречи", "Описание": "Василий Петрович в 14-30"},
    {"Имя": "Петр", "Заголовок": "Машина", "Описание": "Съездить на ТО"},
    {"Имя": "Василий", "Заголовок": "В дорогу", "Описание": "Чемодан, костюм, плавки"}
]

while True:
    # отображение списка заметок
    if notes:
        print("Текущие заметки:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. Имя: {note['Имя']}\n   Заголовок: {note['Заголовок']}\n   Описание: {note['Описание']}")
    else:
        print("Заметок нет.")
    # вводим критерий или выходим из программы
    criter = input("\nВведите имя пользователя или заголовок для удаления заметки (или 'выход' для завершения): ")
    if criter.lower() == "выход":
        print("Программа завершена.")
        break
    # удаление заметок по критерию
    initial_length = len(notes) # запоминаем количество заметок
    # заносим в список только те записи, которые не удовлетворяют критерию
    notes = [note for note in notes if note["Имя"].lower() != criter.lower() and note["Заголовок"].lower() != criter.lower()]
    if len(notes) < initial_length: # если длина списка изменилась, то какие-то записи удалены
        print("Успешно удалено. Остались следующие заметки:")
    else:
        print("Заметок с таким именем пользователя или заголовком не найдено.")
    print()