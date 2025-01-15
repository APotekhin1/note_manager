# Функция добавляет обработку ошибок в функцию работы с файлами
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
        # Создаём файл, если он отсутствует
        with open(filename, 'w') as file:
            pass
        print(f"Файл {filename} не найден. Создан новый файл.")
    except ValueError:
        print(f"Ошибка при чтении файла {filename}. Проверьте его содержимое.")
    except Exception as e:
        print(f"Произошла ошибка при работе с файлом {filename}: {e}")

    return notes


filename = "notes.txt"
print(load_notes_from_file(filename))