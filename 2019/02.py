from __future__ import print_function

def opstream(handle):
    for line in handle:
        for part in line.split(','):
            if part.strip():
                yield int(part)

def main(argv):
    with open(argv[1], 'r') as handle:
        inputs = list(opstream(handle))
    target = int(argv[2])

    # Run gravity assist program 1202
    for verb in range(100):
        for noun in range(100):
            copied_input = list(inputs)
            copied_input[1:3] = [noun, verb]
            a = answer(copied_input)
            if a == target:
                print("%02d%02d" % (noun, verb))
                return
    else:
        print("ERROR: no noun/verb found")

def answer(inputs):
    pos = 0
    while True:
        opcode, a, b, c = inputs[pos:pos+4]
        if opcode == 1:
            inputs[c] = inputs[a] + inputs[b]
            pos += 4
        elif opcode == 2:
            inputs[c] = inputs[a] * inputs[b]
            pos += 4
        elif opcode == 99:
            break
        else:
            raise Exception("illegal opcode %s at position %s: %s" % (opcode, pos, ','.join(str(i) for i in inputs)))
    return inputs[0]


if __name__ == '__main__':
    import sys
    main(sys.argv)
