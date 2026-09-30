'''
1. описание функции count_errors(lines)
2. задать счетчик errors = 0
3. пройтись циклом по линиям
4. если в линиях есть "ERROR", то добавляем к счетчику 1
5. возвращаем errors
'''

def count_errors(lines):
    errors = 0
    for line in lines:
        if "ERROR" in line:
            errors += 1
    return errors

logs = ["INFO: сервер запущен",
    "ERROR: соединение потеряно",
    "INFO: пользователь вошел",
    "ERROR: файл не найден"]
print(count_errors(logs))


