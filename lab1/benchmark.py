import argparse
import sys
import time
from arrays_io import check_count, read_values
from modules.fill import Module as Fill
from modules.sort import Module as Sort

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--count', type=int, default=1000)
    group.add_argument('-i', '--input', type=str)
    parser.add_argument('--seed', type=int, default=1)
    parser.add_argument('--order', choices=['asc', 'desc'], default='asc')
    args = parser.parse_args()

    try:
        if args.input is not None:
            values = read_values(args.input)
        else:
            check_count(args.count)
            generator = Fill(parser)
            values = generator._fill(args.count, seed=args.seed)

        sorter = Sort(parser)
        descending = args.order == 'desc'
        results = []
        for name, method in sorter.METHODS.items():
            numbers = values.copy()
            start = time.time()
            method(numbers, descending)
            elapsed = time.time() - start
            results.append((name, elapsed))
    except (ValueError, OSError) as e:
        print('ОШИБКА:', e, file=sys.stderr)
        return 1

    results.sort(key=lambda x: x[1])
    print(f"Количество элементов: {len(values)}")
    print('Сортировки от самой быстрой до самой медленной:')
    for i, (name, elapsed) in enumerate(results, 1):
        print(f"{i}. {name}: {elapsed:.6f} с")
    return 0

if __name__ == '__main__':
    sys.exit(main())
