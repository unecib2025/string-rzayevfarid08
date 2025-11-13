# all_tasks.py
# Все 10 заданий в одном файле — каждое задание отдельной функцией.
# Код написан просто, без сложных конструкций.

# Задание 1
def task1_check_name():
    name = input("Задание 1. Введите имя: ")
    name = name.strip()
    if name.isalnum():
        name = name.lower()
        print("Имя корректно")
        print("Преобразованное имя:", name)
    else:
        print("Ошибка")

# Задание 2
def task2_check_password():
    password = input("Задание 2. Введите пароль: ")
    has_digit = False
    has_upper = False
    i = 0
    while i < len(password):
        ch = password[i]
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True
        i = i + 1
    if len(password) >= 8 and has_digit and has_upper:
        print("Пароль надёжен")
    else:
        print("Пароль слаб")

# Задание 3
def task3_format_log():
    log = "ACCESS DENIED"
    result = log.capitalize() + " – вход запрещён"
    print("Задание 3. Результат:")
    print(result)

# Задание 4
def task4_filter_logs():
    data = "ERROR connection ERROR failed access"
    replaced = data.replace("ERROR", "ALERT")
    count_alerts = replaced.count("ALERT")
    print("Задание 4. Результат замены:")
    print(replaced)
    print("Количество предупреждений:", count_alerts)

# Задание 5
def task5_email_analysis():
    email = input("Задание 5. Введите email: ")
    if "@" in email:
        parts = email.split("@")
        if len(parts) == 2:
            print("Домен:", parts[1])
        else:
            print("Некорректный адрес")
    else:
        print("Некорректный адрес")

# Задание 6
def task6_normalize_text():
    text = input("Задание 6. Введите текст: ")
    text = text.strip()
    text = text.lower()
    text = text.replace(" ", "_")
    print("Нормализованный текст:", text)

# Задание 7
def task7_privacy_check():
    text = input("Задание 7. Введите сообщение: ")
    if "SECRET" in text:
        text2 = text.replace("SECRET", "******")
        print(text2)
        print("Обнаружена секретная информация!")
    else:
        print("Сообщение безопасно.")

# Задание 8
def task8_codes_roundtrip():
    word = input("Задание 8. Введите слово: ")
    codes_str = ""
    i = 0
    while i < len(word):
        ch = word[i]
        codes_str = codes_str + str(ord(ch)) + " "
        i = i + 1
    print("Коды символов:", codes_str.strip())

    decoded = ""
    parts = codes_str.split()
    j = 0
    while j < len(parts):
        code = parts[j]
        decoded = decoded + chr(int(code))
        j = j + 1
    print("Восстановленное слово:", decoded)

# Задание 9
def task9_find_suspicious():
    text = "login attempt failed access denied unauthorized access"
    failed_count = text.count("failed")
    denied_count = text.count("denied")
    print("Задание 9. counts -> failed:", failed_count, "denied:", denied_count)
    if failed_count > 0 or denied_count > 0:
        print("Попытка несанкционированного доступа!")
    else:
        print("Система в порядке.")

# Задание 10
def task10_report_analysis():
    report = input("Задание 10. Введите отчёт: ")
    sentences = report.split(".")
    count_sentences = 0
    i = 0
    while i < len(sentences):
        s = sentences[i]
        if s.strip() != "":
            count_sentences = count_sentences + 1
        i = i + 1

    no_spaces = report.replace(" ", "")
    count_chars = len(no_spaces)

    starts = False
    if report.lower().startswith("report"):
        starts = True

    error_count = report.lower().count("error")

    print("Количество предложений:", count_sentences)
    print("Количество символов без пробелов:", count_chars)
    if starts:
        print("Начинается с 'Report': Да")
    else:
        print("Начинается с 'Report': Нет")
    if error_count >= 2:
        print("Ошибки найдены")
    else:
        print("Ошибок нет")


# 1. Что представляет собой строка в Python?
# Строка — это последовательность символов, заключённых в кавычки.
# Пример: s = "Привет"

# 2. Что такое Unicode и зачем он используется?
# Unicode — это стандарт, который присваивает каждому символу уникальный номер.
# Он нужен, чтобы можно было работать с текстом на любом языке мира.
# Пример: ord('A') → 65, ord('Ж') → 1046

# 3. Что делают методы strip(), replace(), find()?
# strip() — убирает пробелы по краям строки. Пример: "  hi  ".strip() → "hi"
# replace(a, b) — заменяет все вхождения a на b. Пример: "cat".replace("c", "r") → "rat"
# find(x) — возвращает позицию подстроки или -1, если не найдено. Пример: "hello".find("e") → 1

# 4. Как посчитать количество вхождений подстроки?
# Использовать метод count(). Пример: "apple apple orange".count("apple") → 2

# 5. Чем отличается upper() от capitalize()?
# upper() — делает все буквы заглавными. Пример: "hello".upper() → "HELLO"
# capitalize() — делает первую букву заглавной, остальные маленькими. Пример: "hELLO".capitalize() → "Hello"

# 6. Что возвращает ord() и chr()?
# ord('A') — возвращает числовой код символа. Пример: ord('A') → 65
# chr(65) — возвращает символ по его коду. Пример: chr(65) → "A"

# 7. Как проверить, начинается ли строка с определённого слова?
# Использовать метод startswith(). Пример: "Report started".startswith("Report") → True

# 8. Почему важно фильтровать вводимые пользователем данные?
# Чтобы защитить программу от ошибок и взломов.
# Без фильтрации пользователь может ввести вредный код, неправильные данные
# или попытаться получить доступ к системе.
# Поэтому ввод всегда нужно проверять и очищать.

