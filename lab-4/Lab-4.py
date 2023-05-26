+while True:
    # Запит шляху до файлу
    filepath = input("Введіть шлях до файлу: ")

    try:
        # Відкриття файлу
        with open(filepath, 'r') as f:
            # Ініціалізація змінних статистики
            total_lines = 0
            empty_lines = 0
            lines_with_z = 0
            z_count = 0
            lines_with_and = 0

            # Обробка кожного рядка у файлі
            for line in f:
                total_lines += 1
                line = line.strip()

                if line == "":
                    empty_lines += 1
                elif "z" in line:
                    lines_with_z += 1
                    z_count += line.count("z")
                if "and" in line:
                    lines_with_and += 1

            # Друк статистики
            print("Файл:", filepath)
            print("Загальна кількість рядків:", total_lines)
            print("Кількість порожніх рядків:", empty_lines)
            print("Кількість рядків з літерою 'z':", lines_with_z)
            print("Кількість літер 'z' у файлі:", z_count)
            print("Кількість рядків з групою символів 'and':", lines_with_and)

    except FileNotFoundError:
        print("Файл не знайдено")

    # Запит, чи потрібно аналізувати ще один файл
    another_file = input("Аналізувати ще один файл? (y/n): ")
    if another_file.lower() != "y":
        break