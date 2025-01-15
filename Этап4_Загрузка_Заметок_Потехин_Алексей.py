# Функция читает заметки из текстового файла в формате YAML.
# Преобразует данные в список словарей.
def load_notes_from_file(filename):
    notes = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            note = {}
            for line in file:
                line = line.strip()
                if line.startswith("Имя пользователя:"):
                    note['Имя пользователя'] = line.split(": ", 1)[1]
                elif line.startswith("Заголовок:"):
                    note['Заголовок'] = line.split(": ", 1)[1]
                elif line.startswith("Описание:"):
                    note['Описание'] = line.split(": ", 1)[1]
                elif line.startswith("Статус:"):
                    note['Статус'] = line.split(": ", 1)[1]
                elif line.startswith("Дата создания:"):
                    note['Дата создания'] = line.split(": ", 1)[1]
                elif line.startswith("Дедлайн:"):
                    note['Дедлайн'] = line.split(": ", 1)[1]
                elif line == "---":
                    if note:
                        notes.append(note)
                        note = {}
            # Добавляем последнюю заметку, если нет завершающего "---"
            if note:
                notes.append(note)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")

    return notes

filename = "notes.txt"
print(load_notes_from_file(filename))