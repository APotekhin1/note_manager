from datetime import datetime

def create_note():
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
        "Имя пользователя": username,
        "Заголовок": title,
        "Описание": content,
        "Статус": status,
        "Дата создания": created_date,
        "Дедлайн": issue_date
    }
    return note

def display_notes(notes, page_size=5):
    # Функция для отображения списка заметок постранично.
    if not notes:
        print("У вас нет сохранённых заметок.")
        return
    total_notes = len(notes)
    total_pages = (total_notes + page_size - 1) // page_size  # Вычисляем количество страниц
    current_page = 1
    while True:
        # Определяем границы заметок для текущей страницы
        start_i = (current_page - 1) * page_size
        end_i = start_i + page_size
        current_notes = notes[start_i:end_i]
        print(f"\nСписок заметок (Страница {current_page} из {total_pages}):")
        print("-" * 30)
        # вывод элементов списка на текущей странице
        for i, note in enumerate(current_notes, start=start_i + 1):
            print(f"Заметка №{i}:")
            print(f"Имя пользователя: {note.get('Имя пользователя', 'Не указано')}")
            print(f"Заголовок: {note.get('Заголовок', 'Нет заголовка')}")
            print(f"Описание: {note.get('Описание', 'Нет описания')}")
            print(f"Статус: {note.get('Статус', 'Не указан')}")
            print(f"Дата создания: {note.get('Дата создания', 'Не указана')}")
            print(f"Дедлайн: {note.get('Дедлайн', 'Не указан')}")
            print("-" * 30)
        # Проверка на последнюю страницу
        if current_page == total_pages:
            print("Вы достигли конца списка заметок.")
        else:
            print("Для перехода к следующей странице введите 'n', для выхода — 'q'.")
        # Обработка ввода
        user_input = input("\nВведите команду (n - следующая, p - предыдущая, q - выход): ").strip().lower()
        if user_input == 'n' and current_page < total_pages:
            current_page += 1
        elif user_input == 'p' and current_page > 1:
            current_page -= 1
        elif user_input == 'q':
            print("Выход из режима просмотра заметок.")
            break
        else:
            print("Неверная команда. Попробуйте снова.")

def update_note(note):
    # Доступные поля для обновления
    editable_fields = ["Имя пользователя", "Заголовок", "Описание", "Статус", "Дедлайн"]
    while True:
        # Выводим пользователю доступные для обновления поля
        field_to_update = input(f"Какие данные вы хотите обновить? ({', '.join(editable_fields)}): ")
        if field_to_update in editable_fields:
            # Запрос нового значения для выбранного поля
            if field_to_update == "Дедлайн":
                while True:
                    new_value = input("Введите новое значение для issue_date (день-месяц-год): ")
                    try:
                        # Проверяем корректность формата даты
                        datetime.strptime(new_value, "%d-%m-%Y")
                        break
                    except ValueError:
                        print("Неверный формат даты. Попробуйте ещё раз.")
            else:
                new_value = input(f"Введите новое значение для {field_to_update}: ")
            # Обновляем поле заметки
            note[field_to_update] = new_value
            print("Обновленная заметка:")
            print(note)
            return note
        else:
            print("Некорректное имя поля. Пожалуйста, выберите одно из доступных полей.")

def delete_note(notes):
    # Функция удаления заметок
    if not notes:
        print("Список заметок пуст.")
        return
    # вводим критерий или выходим из программы
    criter = input("\nВведите имя пользователя или заголовок для удаления заметки (или 'выход' для завершения): ")
    if criter.lower() == "выход":
        print()
        return
    # удаление заметок по критерию
    initial_length = len(notes) # запоминаем количество заметок
    # заносим в список только те записи, которые не удовлетворяют критерию
    notes = [note for note in notes if note["Имя пользователя"].lower() != criter.lower() and note["Заголовок"].lower() != criter.lower()]
    if len(notes) < initial_length: # если длина списка изменилась, то какие-то записи удалены
        print("Успешно удалено")
    else:
        print("Заметок с таким именем пользователя или заголовком не найдено.")
    print()

def search_notes(notes, keyword=None, status=None):
    # Функция поиска заметок
    if not notes:
        print("Список заметок пуст.")
        return
    # Фильтруем заметки по ключевому слову и статусу
    filtered_notes = []
    for note in notes:
        matches_keyword = (
            keyword is None or
            keyword.lower() in note['Заголовок'].lower() or
            keyword.lower() in note['Описание'].lower() or
            keyword.lower() in note['Имя пользователя'].lower()
        )
        matches_status = (status is None or note['Статус'] == status)
        if matches_keyword and matches_status:
            filtered_notes.append(note)
    # Вывод результата
    if filtered_notes:
        print("Найдены заметки:")
        for i, note in enumerate(filtered_notes, start=1):
            print(f"\nЗаметка №{i}:")
            print(f"Имя пользователя: {note['Имя пользователя']}")
            print(f"Заголовок: {note['Заголовок']}")
            print(f"Описание: {note['Описание']}")
            print(f"Статус: {note['Статус']}")
    else:
        print("Заметки, соответствующие запросу, не найдены.")


# Запуск программы
if __name__ == "__main__":
    notes = []
    while True:
        print("""
        Меню действий:
        1. Создать новую заметку
        2. Показать все заметки
        3. Обновить заметку
        4. Удалить заметку
        5. Найти заметки
        6. Выйти из программы
        """)
        choice = input("Ваш выбор: ")
        if choice == "1":
            note = create_note()
            notes.append(note)
        elif choice == "2":
            display_notes(notes)
        elif choice == "3":
            if notes:
                display_notes(notes)
                index = int(input("Введите номер заметки для обновления: ")) - 1
                if 0 <= index < len(notes):
                    notes[index] = update_note(notes[index])
                else:
                    print("Неверный номер заметки.")
            else:
                print("Список заметок пуст.")
        elif choice == "4":
            # удаление заметок по введенному критерию
            delete_note(notes)
        elif choice == "5":
            keyword = input("Введите ключевое слово для поиска: ")
            status = input("Введите статус для поиска (или оставьте пустым): ")
            found_notes = search_notes(notes, keyword, status)
            display_notes(found_notes)
        elif choice == "6":
            print("Программа завершена. Спасибо за использование!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")