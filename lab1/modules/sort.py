import argparse
import sys
from AbsClass import Module
from arrays_io import MIN_VALUE, MAX_VALUE, read_values, write_values

class Module(Module):
    def __init__(self, parser: argparse.ArgumentParser):
        self.parser = parser
        self.METHODS = {
            'bubble': self._bubble,
            'selection': self._selection,
            'insertion': self._insertion,
            'counting': self._counting
        }

    def register(self):
        self.parser.add_argument('-m', '--method', choices=self.METHODS, required=True)
        self.parser.add_argument('--order', choices=['asc', 'desc'], default='asc')
        self.parser.add_argument('-i', '--input', type=str)
        self.parser.add_argument('-o', '--output', type=str)

    def run(self, args):
        try:
            values = read_values(args.input)
            method = self.METHODS[args.method]
            descending = args.order == 'desc'
            method(values, descending)
            write_values(values, args.output)
        except (ValueError, OSError) as e:
            print('ОШИБКА:', e, file=sys.stderr)
            return 1
        print('Массив отсортирован.')
        return 0

    def _out_of_order(self, a, b, descending):
        if descending:
            return a < b
        return a > b

    def _bubble(self, values, descending=False):
        n = len(values)
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                if self._out_of_order(values[j], values[j + 1], descending):
                    values[j], values[j + 1] = values[j + 1], values[j]
                    swapped = True
            if not swapped:
                break

    def _selection(self, values, descending=False):
        n = len(values)
        for i in range(n - 1):
            best = i
            for j in range(i + 1, n):
                if self._out_of_order(values[best], values[j], descending):
                    best = j
            values[i], values[best] = values[best], values[i]

    def _insertion(self, values, descending=False):
        n = len(values)
        for i in range(1, n):
            current = values[i]
            j = i
            while j > 0 and self._out_of_order(values[j - 1], current, descending):
                values[j] = values[j - 1]
                j -= 1
            values[j] = current

    def _counting(self, values, descending=False):
        counts = [0] * (MAX_VALUE - MIN_VALUE + 1)
        for value in values:
            counts[value - MIN_VALUE] += 1
        k = 0
        numbers = range(len(counts))
        if descending:
            numbers = reversed(numbers)
        for number in numbers:
            for i in range(counts[number]):
                values[k] = number + MIN_VALUE
                k += 1
