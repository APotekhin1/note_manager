from datetime import datetime # включаем библиотеки datetime для работы с датами

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