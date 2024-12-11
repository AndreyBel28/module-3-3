# Домашнее задание по уроку "Распаковка позиционных параметров"
def print_params(a=1, b='строка', c=True):
    # Печатаем значения параметров
    print(a, b, c)


# Вызовы функции с разным количеством аргументов
print_params()
print_params(10)
print_params(10, 'новая строка')
print_params(b=25)
print_params(c=[1, 2, 3])

# 2. Распаковка параметров
values_list = [3.14, 'пример', False]  # Список значений
values_dict = {'a': 42, 'b': 'текст', 'c': None}  # Словарь значений

# Используем распаковку списка и словаря для передачи параметров
print_params(*values_list)
print_params(**values_dict)
# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']  # Другой список значений
print_params(*values_list_2, 42)
