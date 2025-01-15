import json

# Создаем функцию, которая сохраняет список заметок в формате JSON.
def save_notes_json(notes, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        print(f"Заметки успешно сохранены в файл {filename} в формате JSON.")
    except Exception as e:
        print(f"Произошла ошибка при сохранении заметок в файл {filename}: {e}")

# Пример ввода данных
notes = [
    {
        "Имя пользователя": "Сергей",
        "Заголовок": "Продукты",
        "Описание": "Купить по списку",
        "Статус": "В процессе",
        "Дата создания": "2025-01-10",
        "Дедлайн": "2025-01-17"
    },
    {
        "Имя пользователя": "Марина",
        "Заголовок": "Спорт. клуб",
        "Описание": "Взять скакалку",
        "Статус": "Готово",
        "Дата создания": "2025-01-11",
        "Дедлайн": "2025-01-15"
    }
]

filename = "notes.json"
save_notes_json(notes, filename)