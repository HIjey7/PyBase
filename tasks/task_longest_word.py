'''
1. описать функцию find_longest_word(words)
2. задать начальное значение longest = ""
3. цикл word in words
4. если длина word > длины longest
5. longest = word
6. вернуть longest
'''

def find_longest_word(words):
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(find_longest_word(['cat', 'elephant', 'bird']))