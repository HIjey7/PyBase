'''
1. описать функцию count_vowels(text)
2. объявить счетчик = 0
3. цикл ch по тексту
4. если в ch есть "aeiou" то счетчик += 1
5. вернуть счетчик
'''

def count_vowels(text):
    count = 0
    vowels = 'aeiou'
    for ch in text:
        if ch.lower() in vowels:
            count += 1
    return count

print(count_vowels("Hello Bratish"))


