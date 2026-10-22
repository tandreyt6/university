import argparse
import sys
import os
import loader

arg_parser = argparse.ArgumentParser()
subparsers = arg_parser.add_subparsers(dest='type', required=True)

path = os.path.join(os.path.dirname(__file__), "modules")
files = [
    file for file in os.listdir(path)
    if os.path.isfile(os.path.join(path, file)) and file.endswith(".py")
]

all_modules = {}
for file in files:
    name = os.path.splitext(file)[0]
    cls = loader.load_file(os.path.join(path, file))
    parser = subparsers.add_parser(name)
    obj = cls(parser)
    obj.register()
    all_modules[name] = obj

args = arg_parser.parse_args()

sys.exit(all_modules[args.type].run(args))
