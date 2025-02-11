# Функция перезаписывает данные файла, записывая список заметок в текстовом формате YAML.
def save_notes_to_file(notes, filename):
    try:
        with open(filename, 'w', encoding="utf-8") as file:
        # цикл перебирает записи и записывает их в файл
            for note in notes:
                file.write(f"Имя пользователя: {note.get('Имя пользователя', '')}\n")
                file.write(f"Заголовок: {note.get('Заголовок', '')}\n")
                file.write(f"Описание: {note.get('Описание', '')}\n")
                file.write(f"Статус: {note.get('Статус', '')}\n")
                file.write(f"Дата создания: {note.get('Дата создания', '')}\n")
                file.write(f"Дедлайн: {note.get('Дедлайн', '')}\n")
                file.write("---\n")
        print(f"Заметки успешно сохранены в файл {filename}.")
    except IOError as e:
        print(f"Ошибка при записи в файл: {e}")

# пример для записи и ввода
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

filename = "notes.txt"
save_notes_to_file(notes, filename)