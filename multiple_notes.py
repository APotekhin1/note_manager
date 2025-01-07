from datetime import date, datetime # включаем библиотеки datetime для работы с датами

answer = input('Добро пожаловать в "Менеджер заметок"! Хотите добавить новую заметку? ')
notes = [] # начальное значение вводимого списка заметок
while answer != 'стоп' and answer != 'нет':
    # ввод текущего элемента
    name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    while True:  # цикл для определения корректной даты ввода
        created_date = input("Введите дату создания (день-месяц-год): ")
        issue_date = input("Введите дедлайн (день-месяц-год): ")
        try:
            created_date = datetime.strptime(created_date, '%d-%m-%Y')
            issue_date = datetime.strptime(issue_date, '%d-%m-%Y')
            break
        except ValueError as e:
            print(e)
    # создание элемента списка в виде словаря
    note = {
        "name": name,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
    }
    notes.append(note)
    answer = input('Хотите добавить еще заметку? ')
# ввывод всех элементов списка, вывод дат в виде ДД-ММ-ГГГГ
print("\nСписок заметок:")
for i in notes:
    print(f"   Имя: {i['name']}")
    print(f"   Заголовок: {i['title']}")
    print(f"   Описание: {i['content']}")
    print(f"   Статус: {i['status']}")
    print("   Дата создания: {}-{}-{}".format(created_date.day, created_date.month, created_date.year))
    print("   Дедлайн: {}-{}-{}".format(issue_date.day, issue_date.month, issue_date.year))
