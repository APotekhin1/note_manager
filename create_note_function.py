from datetime import datetime

def create_note():
    # Функция создает заметку.
       # Запрашиваем имя пользователя
    username = input("Введите имя пользователя: ")
    # Запрашиваем заголовок заметки
    title = input("Введите заголовок заметки: ")
    # Запрашиваем описание заметки
    content = input("Введите описание заметки: ")
    # Запрашиваем статус заметки
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    # Получаем текущую дату в формате день-месяц-год
    created_date = datetime.now().strftime("%d-%m-%Y")
    # Запрашиваем дату дедлайна с проверкой корректности формата
    while True:
        issue_date = input("Введите дату дедлайна (день-месяц-год): ")
        try:
            # Пробуем преобразовать введённую дату
            datetime.strptime(issue_date, "%d-%m-%Y")
            break
        except ValueError:
            print("Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год (например, 30-11-2024).")
    # Формируем поле словаря заметки
    note = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
    }
    return note

# Демонстрация работы функции
if __name__ == "__main__":
    note = create_note()
    print("Созданная заметка:", note)