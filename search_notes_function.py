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
            keyword.lower() in note['title'].lower() or
            keyword.lower() in note['content'].lower() or
            keyword.lower() in note['username'].lower()
        )
        matches_status = (status is None or note['status'] == status)

        if matches_keyword and matches_status:
            filtered_notes.append(note)

    # Вывод результата
    if filtered_notes:
        print("Найдены заметки:")
        for i, note in enumerate(filtered_notes, start=1):
            print(f"\nЗаметка №{i}:")
            print(f"Имя пользователя: {note['username']}")
            print(f"Заголовок: {note['title']}")
            print(f"Описание: {note['content']}")
            print(f"Статус: {note['status']}")
    else:
        print("Заметки, соответствующие запросу, не найдены.")

# Пример использования функции
notes = [
    {
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27-11-2024',
        'issue_date': '30-11-2024'
    },
    {
        'username': 'Мария',
        'title': 'Учеба',
        'content': 'Подготовиться к экзамену',
        'status': 'в процессе',
        'created_date': '25-11-2024',
        'issue_date': '01-12-2024'
    },
    {
        'username': 'Иван',
        'title': 'План работы',
        'content': 'Завершить проект',
        'status': 'выполнено',
        'created_date': '20-11-2024',
        'issue_date': '26-11-2024'
    }
]

# Тестирование функции
if __name__ == "__main__":
    search_notes(notes, keyword='покупок')
    search_notes(notes, status='в процессе')
    search_notes(notes, keyword='работы', status='выполнено')
