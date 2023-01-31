Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
try:
    number = input('Введите числа через пробел: ')
    us_num = input('Введите любое число: ')
    if ',' in number:
        print("Введите числа в соответствии с условиями ввода. Перезапустите программу и повторите ввод.")
    if type(us_num) != int:
        print("Вы ввели число, не соответствующее цифровому формату ввода. Перезапустите программу и повторите ввод.")
    except ValueError:
        
SyntaxError: invalid syntax
except ValueError:
    
SyntaxError: invalid syntax
except
SyntaxError: incomplete input
except ValueError:
    
SyntaxError: invalid syntax
print("Пожалуйста, перезапустите программу и повторите ввод в соответствии с условиями.")
Пожалуйста, перезапустите программу и повторите ввод в соответствии с условиями.
>>> 1
1
>>> try:
...     number = input('Введите числа через пробел: ')
...     us_num = int(input('Введите любое число: '))
...     if ',' in number:
...         print("Введите числа в соответствии с условиями ввода. Перезапустите программу и повторите ввод.")
...         except ValueError:
...             
SyntaxError: invalid syntax
>>> try:
...     number = input('Введите числа через пробел: ')
...     us_num = input('Введите любое число: ')
...     f ',' in number:
...         
SyntaxError: invalid syntax
>>>     if ',' in number:
...         
SyntaxError: unexpected indent
>>> try:
...     number = input('Введите числа через пробел: ')
...     us_num = input('Введите любое число: ')
...     if ',' in number:
...         print("Введите числа в соответствии с условиями ввода. Перезапустите программу и повторите ввод.")
...     if type(us_num) != int:
...         print("Вы ввели число, не соответствующее цифровому формату ввода. Перезапустите программу и повторите ввод.")
... except ValueError:
...         print("Пожалуйста, перезапустите программу и повторите ввод в соответствии с условиями.")
... 
...         
Введите числа через пробел: 1 4 5 6
Введите любое число: one
Вы ввели число, не соответствующее цифровому формату ввода. Перезапустите программу и повторите ввод.
>>> 
>>> 
>>> 2
2
>>> \
... 
