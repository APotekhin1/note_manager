def create_note():
    print("\nСоздание новой заметки...")
    # Логика для создания заметки
    print("Новая заметка создана!")

def display_notes():
    print("\nСписок всех заметок:")
    # Логика для отображения всех заметок

def update_note():
    print("\nОбновление заметки...")
    # Логика для обновления заметки

def delete_note():
    print("\nУдаление заметки...")
    # Логика для удаления заметки

def search_notes():
    print("\nПоиск заметки...")
    # Логика для удаления заметки

def main_menu():
    while True:
        print("\nМеню действий:")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы")

        try:
            choice = int(input("\nВаш выбор: "))
            if choice == 1:
                create_note()
            elif choice == 2:
                display_notes()
            elif choice == 3:
                update_note()
            elif choice == 4:
                delete_note()
            elif choice == 5:
                search_notes()
            elif choice == 6:
                print("\nПрограмма завершена. Спасибо за использование!")
                break
            else:
                print("\nНеверный выбор. Пожалуйста, выберите действие из списка.")
        except ValueError:
            print("\nОшибка: Введите число от 1 до 6.")

# Запуск программы
main_menu()
