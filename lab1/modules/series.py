import argparse
from math import isfinite
from AbsClass import Module

class Module(Module):
    def __init__(self, parser: argparse.ArgumentParser):
        self.parser = parser

    def register(self):
        self.parser.add_argument('--func', choices=['third', 'sqplus'], required=True)
        group = self.parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--terms', type=int)
        group.add_argument('--eps', type=float)

    def run(self, args):
        try:
            if args.terms is not None and not 1 <= args.terms <= 10000:
                raise ValueError("Invalid terms!")
            if args.eps is not None and not (isfinite(args.eps) and 0 < args.eps <= 0.0001):
                raise ValueError("Invalid eps!")
            total, n = self._solve(args)
        except ValueError as e:
            print("Программа упала:", e)
            return 1
        print("Слагаемых:", n)
        print("Сумма ряда:", f"{total:.4f}")
        return 0

    def _solve(self, args):
        total, n = 0, 0
        while True:
            n += 1
            x = 1 / (3*n) if args.func == 'third' else 1 / (n**2 + 1)
            x *= (-1)**(n+1)
            total += x
            if args.terms is not None and n >= args.terms:
                break
            if args.eps is not None and abs(x) < args.eps:
                break
        return total, n