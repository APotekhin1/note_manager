from datetime import datetime

def update_note(note):
    # Функция для обновления полей заметки.
    print("Текущие данные заметки:")
    print(note)
    # Доступные поля для обновления
    editable_fields = ["username", "title", "content", "status", "issue_date"]
    while True:
        # Выводим пользователю доступные для обновления поля
        field_to_update = input(f"Какие данные вы хотите обновить? ({', '.join(editable_fields)}): ")
        if field_to_update in editable_fields:
            # Запрос нового значения для выбранного поля
            if field_to_update == "issue_date":
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


# Пример заметки
sample_note = {
    "username": "Алексей",
    "title": "Список покупок",
    "content": "Купить продукты на неделю",
    "status": "новая",
    "created_date": "27-11-2024",
    "issue_date": "30-11-2024"
    }
# Вызываем функцию для обновления заметки
if __name__ == "__main__":
    updated_note = update_note(sample_note)