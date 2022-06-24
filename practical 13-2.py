'''
Практическая №13
Вариант №32
2. Из заданной строки отобразить только символы пунктуации. Использовать
библиотеку string.
Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"
'''
import string
str = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'

new_str = list(filter(lambda ch: ch in string.punctuation+string.whitespace, str))

print(' '.join(new_str))