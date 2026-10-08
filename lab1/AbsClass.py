import argparse
from typing import List, Tuple

class Module:
    def __init__(self, parser: argparse.ArgumentParser):
        self.parser = parser
        raise NotImplementedError()

    def register(self):
        raise NotImplementedError()

    def run(self, args):
        raise NotImplementedError()
