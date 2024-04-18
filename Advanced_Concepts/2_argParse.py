# argparse -> Support Command Line Arguements
import argparse


parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n",default=1,help="Number of times to print meow", type=int)
args = parser.parse_args()

# for _ in range(int(args.n)): # if we don't specify in `type=int` in `parser.add_argument`
for _ in range(args.n):
    print("meow")