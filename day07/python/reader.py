def parse(line):
    parts = line.split("contain")
    left = parts[0]
    right = parts[1]
    parts = left.split()
    left_key = f"{parts[0]}_{parts[1]}"
    lst = []
    for part in right.split(","):
        pieces = part.split()
        try:
            number = int(pieces[0])
        except ValueError:
            break
        key = f"{pieces[1]}_{pieces[2]}"
        lst.append((number, key))
    #
    return (left_key, lst)


def process(fname):
    with open(fname) as f:
        lines = f.read().splitlines()

    d = {}
    for line in lines:
        key, lst = parse(line)
        d[key] = lst
    #
    return d
