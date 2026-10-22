import sys

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1000000

def check_count(count):
    if not 1 <= count <= MAX_COUNT:
        raise ValueError(f"количество элементов вне диапазона 1..{MAX_COUNT}")

def check_values(values):
    check_count(len(values))
    if any(x < MIN_VALUE or x > MAX_VALUE for x in values):
        raise ValueError(f"значения вне диапазона {MIN_VALUE}..{MAX_VALUE}")

def read_values(path):
    if path is not None:
        with open(path, encoding='utf-8-sig') as f:
            text = f.read()
    else:
        lines = []
        print('Введите числа. Пустая строка завершает ввод.', file=sys.stderr)
        while True:
            try:
                line = input()
            except EOFError:
                break
            if not line.strip():
                break
            lines.append(line)
        text = ' '.join(lines)
    try:
        values = [int(x) for x in text.replace(',', ' ').split()]
    except ValueError:
        raise ValueError('массив должен содержать только целые числа') from None
    check_values(values)
    return values

def write_values(values, path):
    text = ' '.join(str(x) for x in values)
    if path is None:
        print(text)
    else:
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text + '\n')
        print(f"Записано элементов: {len(values)} в файл {path}")
