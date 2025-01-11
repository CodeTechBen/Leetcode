"""find the nth number in the fibonacci sequence
Sequence: 
n, num
1, 0,
2, 1,
3, 1,
4, 2,
5, 3,
6, 5,
7, 8,
8, 13,
9, 21,
10,34,
11,55
"""
from argparse import ArgumentParser, Namespace

def parsing_command_line_inputs() -> Namespace:
    """Handle command-line arguments and parsing."""
    parser = ArgumentParser()
    parser.add_argument(
        "--num", "-n", help="nth term of the fibonacci sequence", required=True)
    return parser.parse_args()

def fib(n: int) -> int:
    """find the nth number in the fibonacci sequence"""
    sequence = [0, 1]
    print(sequence)
    while n > len(sequence):
        sequence.append(get_next(sequence[-2], sequence[-1]))
        print(sequence)
    return sequence[n-1]
    
def get_next(num_1: int, num_2: int) -> int:
    """returns the next number of the fibonacci sequence"""
    return num_1 + num_2


if __name__ == "__main__":
    args = parsing_command_line_inputs()
    print(fib(int(args.num)))
