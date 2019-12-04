from __future__ import print_function

def opstream(handle):
    for line in handle:
        for part in line.split(','):
            if part.strip():
                yield int(part)

def groups(iterator, size):
    try:
        yield tuple(int(iterator.next()) for _ in range(size))
    except:
        return

def main(argv):
    with open(argv[1], 'r') as handle:
        inputs = list(opstream(handle))
    pos = 0

    # Run gravity assist program 1202
    inputs[1] = 12
    inputs[2] = 2

    while True:
        opcode, a, b, c = inputs[pos:pos+4]
        print("%s: %s, %s, %s, %s" % (','.join(str(i) for i in inputs), opcode, a, b, c))
        if opcode == 1:
            inputs[c] = inputs[a] + inputs[b]
        elif opcode == 2:
            inputs[c] = inputs[a] * inputs[b]
        elif opcode == 99:
            break
        else:
            raise Exception("illegal opcode %d at position %d: %s", opcode, pos, ','.join(inputs))
        pos += 4
    print(inputs[0])


if __name__ == '__main__':
    import sys
    main(sys.argv)
