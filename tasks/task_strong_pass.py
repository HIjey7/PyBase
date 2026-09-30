'''
1. описать функцию is_strong_password(password)
2. завести has_digit = False и has_upper = False
3. пройти циклом по каждому символу пароля
4. если текущий символ — цифра → has_digit = True
5. если текущий символ — заглавная → has_upper = True
6. вернуть True только если длина >= 8 И оба флага True
'''

def is_strong_password(password):
    has_digit = False
    has_upper = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True
    return True if len(password) >= 8 and has_digit and has_upper else False

print(is_strong_password("asdasd"))
print(is_strong_password("Qwerty123"))
print(is_strong_password("QwertyNetuas"))

