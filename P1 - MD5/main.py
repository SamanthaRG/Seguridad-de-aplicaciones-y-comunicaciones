import argparse

argp = argparse.ArgumentParser()
argp.add_argument('instr', type=str)

args = argp.parse_args()
print(args.in_str)

# python .\md5.py qewqe
