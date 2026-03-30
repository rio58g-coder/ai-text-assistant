# main.py
# Основной файл проекта — меню и интерфейс

from ai_utils import summarize_text, rewrite_text, chat_response

def menu():
    print("\n=== AI Text Assistant ===")
    print("1. Суммаризация текста")
    print("2. Переписать текст")
    print("3. Чат с ИИ")
    print("0. Выход")


def main():
    while True:
        menu()
        choice = input("Выбери действие: ")

        if choice == "1":
            text = input("Введи текст: ")
            print("\nРезультат:")
            print(summarize_text(text))

        elif choice == "2":
            text = input("Введи текст: ")
            print("\nРезультат:")
            print(rewrite_text(text))

        elif choice == "3":
            text = input("Ты: ")
            print("ИИ:", chat_response(text))

        elif choice == "0":
            print("Выход. Пока!")
            break

        else:
            print("Неверный выбор, попробуй снова.")


if __name__ == "__main__":
    main()