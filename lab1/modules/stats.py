import argparse
import os
from typing import List, Tuple
from AbsClass import Module
from math import sqrt

class Module(Module):
    def __init__(self, parser: argparse.ArgumentParser):
        self.parser = parser

    def register(self):
        self.parser.add_argument('-i', '--input', type=str, help='Path to file for check', required=False)

    def get_num_line(self, path: str) -> List[List[int]]:
        if not os.path.exists(path):
            raise FileExistsError(f"File {path} not found!")
        lines = []
        with open(path, "r", encoding="utf-8") as f:
            all_line = "".join(f.read().split("\n"))
            all_line = all_line.split(" ")
            all_line = [int(_) for _ in all_line if _.strip().isdigit()]
            lines.append(all_line)
        return lines

    def run(self, args):
        lines = []
        if args.input is None:
                while 1:
                    l = input(">>>")
                    line = [int(_) for _ in l.split(" ") if _.isdigit()]
                    if l.strip() == "":
                        break
                    lines.append(line)
                
        else:
            lines = self.get_num_line(args.input)
        line = []
        for el in lines:
            for i in el:
                line.append(i)
        n = len(line)
        total = sum(line)
        mean = total / n
        sum_squares = sum(x ** 2 for x in line)
        mean_square = sqrt(sum_squares / n)
        squared_deviations = sum((x - mean) ** 2 for x in line)
        variance = squared_deviations / n
        sko = sqrt(variance)
        std = sqrt(squared_deviations / (n - 1)) if n > 1 else None
        minimum = min(line)
        maximum = max(line)
        positive = sum(x > 0 for x in line)
        negative = sum(x < 0 for x in line)

        print("Сумма:", total)
        print("Ср. арифм.:", f"{mean:.3f}")
        print("Сумма квадратов:", sum_squares)
        print("Ср. квадратическое:", f"{mean_square:.3f}")
        print("Дисперсия:", f"{variance:.3f}")
        print("СКО:", f"{sko:.3f}")
        print("Станд. отклонение:", f"{std:.3f}" if std is not None else "не определено")
        print("Минимум:", minimum)
        print("Максимум:", maximum)
        print("Положительных:", positive)
        print("Отрицательных:", negative)
