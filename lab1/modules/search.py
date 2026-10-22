import argparse
import sys
from AbsClass import Module
from arrays_io import read_values

class Module(Module):
    MAX_SEARCH = 1000

    def __init__(self, parser: argparse.ArgumentParser):
        self.parser = parser

    def register(self):
        self.parser.add_argument('-v', '--value', type=int, required=True)
        self.parser.add_argument('-i', '--input', type=str)

    def run(self, args):
        try:
            if abs(args.value) > self.MAX_SEARCH:
                raise ValueError(f"модуль искомого значения больше {self.MAX_SEARCH}")
            values = read_values(args.input)
            if any(values[i] > values[i + 1] for i in range(len(values) - 1)):
                raise ValueError('массив не упорядочен по возрастанию')
            index = self._search(values, args.value)
            if index is None:
                print(f"Значение {args.value} не найдено.", file=sys.stderr)
                return 1
        except (ValueError, OSError) as e:
            print('ОШИБКА:', e, file=sys.stderr)
            return 1
        print(f"Значение {args.value} имеет элемент с индексом {index + 1}.")
        return 0

    def _search(self, values, value):
        left = 0
        right = len(values) - 1
        while left <= right:
            middle = (left + right) // 2
            if values[middle] == value:
                return middle
            if values[middle] < value:
                left = middle + 1
            else:
                right = middle - 1
        return None
