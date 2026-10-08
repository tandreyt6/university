import argparse
import math
import sys
from AbsClass import Module

class Module(Module):
    MIN_STEPS = 1
    MAX_STEPS = 100000

    RATIO_MIN, RATIO_MAX = 0, 20
    ROOT_MIN, ROOT_MAX = -5, 5

    FUNCTIONS = {
        'ratio': ('_ratio', RATIO_MIN, RATIO_MAX, True),
        'root': ('_root', ROOT_MIN, ROOT_MAX, False)
    }

    def __init__(self, parser: argparse.ArgumentParser):
        self.parser = parser

    def register(self):
        self.parser.add_argument('--func', choices=self.FUNCTIONS, required=True)
        self.parser.add_argument('--from', dest='start', type=float, required=True)
        self.parser.add_argument('--to', dest='end', type=float, required=True)
        self.parser.add_argument('--steps', type=int, required=True)

    def run(self, args):
        try:
            method, left, right, closed = self.FUNCTIONS[args.func]

            if not all(map(math.isfinite, [args.start, args.end])):
                raise ValueError("Invalid limits!")
            if args.start >= args.end:
                raise ValueError("Invalid interval!")
            if not self.MIN_STEPS <= args.steps <= self.MAX_STEPS:
                raise ValueError("Invalid steps!")

            if closed:
                valid = left <= args.start < args.end <= right
            else:
                valid = left < args.start < args.end < right

            if not valid:
                raise ValueError("Out of function range!")

            result = self._solve(getattr(self, method), args.start, args.end, args.steps)
        except ValueError as e:
            print("Программа упала:", e, file=sys.stderr)
            return 1
        print("Значение интеграла:", f"{result:.4f}")
        return 0

    @staticmethod
    def _ratio(x):
        return x / (x + 1)

    @staticmethod
    def _root(x):
        return math.sqrt(x**2 + 1)

    def _solve(self, func, start, end, steps):
        h = (end - start) / steps
        return sum(func(start + i*h) * h for i in range(steps))