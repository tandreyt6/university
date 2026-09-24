import math, sys
from typing import List, Tuple

DIS = 2

def _solve(args) -> Tuple[int]|None:
    if None in [args.a, args.b, args.c]:
        raise ValueError("coefficient is missing!")
    if any(map(lambda x: abs(x) > DIS, [args.a, args.b, args.c])):
        raise ValueError("coefficient is too large!")
    a, b, c = args.a, args.b, args.c
    D = b**2 - 4*a*c
    if D < 0:
        return None, None, D
    elif D == 0:
        X1 = -b/2*a
        X2 = X1
        return X1, X2, D
    X1 = (-b + D**0.5)/2*a
    X2 = (-b - D**0.5)/2*a
    return X1, X2, D

def solve(args):
    print(f"Input: {args.a}*X^2 + {args.b}*X + {args.c}")
    try:
        X1, X2, D = _solve(args) or (None, None, None)
    except ValueError as e:
        print("Программа упала:", e)
        sys.exit(1)
    print(f"Output: x1 = {X1:.3f}, x2 = {X2:.3f}, D = {D}" if X1 and X2 else f"X1 and X2 is None, D = {D}")

    sys.exit(0)

all_operations = {
    "solve": solve
}