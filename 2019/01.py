from __future__ import division
from __future__ import print_function

def fuel(mass):
    fuel_mass = mass // 3 - 2
    if fuel_mass <= 0:
        return 0
    return fuel_mass + fuel(fuel_mass)

def main(argv):
    with open(argv[1], 'r') as f:
        answer = sum(fuel(int(line)) for line in f)
    print(answer)

if __name__ == '__main__':
    import sys
    main(sys.argv)
