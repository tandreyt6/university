import argparse
import sys
from lab1.operations import all_operations

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('type', choices=['solve'], help='Select type of operation')
arg_parser.add_argument('-a', type=int, help='The coefficient \'A\'')
arg_parser.add_argument('-b', type=int, help='The coefficient \'B\'')
arg_parser.add_argument('-c', type=int, help='The coefficient \'C\'')

args = arg_parser.parse_args()

if args.type is None:
    arg_parser.print_help()
    sys.exit(0)
if args.type in all_operations:
    all_operations[args.type](args)
    sys.exit(0)
raise ValueError("Unknown operation type")
