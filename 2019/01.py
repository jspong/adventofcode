from __future__ import division
from __future__ import print_function

def fuel(mass):
    return mass // 3 - 2

def main(argv):
    with open(argv[1], 'r') as f:
        answer = sum(fuel(int(line)) for line in f)
    print(answer)

if __name__ == '__main__':
    import sys
    main(sys.argv)
