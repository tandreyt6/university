import argparse
import sys
import random
from AbsClass import Module
from arrays_io import MIN_VALUE, MAX_VALUE, check_count, write_values

class Module(Module):
    def __init__(self, parser: argparse.ArgumentParser):
        self.parser = parser

    def register(self):
        self.parser.add_argument('-c', '--count', type=int, required=True)
        self.parser.add_argument('--min', type=int, default=MIN_VALUE)
        self.parser.add_argument('--max', type=int, default=MAX_VALUE)
        self.parser.add_argument('--seed', type=int)
        self.parser.add_argument('-o', '--output', type=str)

    def run(self, args):
        try:
            check_count(args.count)
            if not MIN_VALUE <= args.min <= args.max <= MAX_VALUE:
                raise ValueError(f"границы должны удовлетворять {MIN_VALUE} <= min <= max <= {MAX_VALUE}")
            values = self._fill(args.count, args.min, args.max, args.seed)
            write_values(values, args.output)
        except (ValueError, OSError) as e:
            print('ОШИБКА:', e, file=sys.stderr)
            return 1
        return 0

    def _fill(self, count, low=MIN_VALUE, high=MAX_VALUE, seed=None):
        random.seed(seed)
        values = []
        for i in range(count):
            values.append(random.randint(low, high))
        return values
