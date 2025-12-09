
def solve_part2(filename):
    """
    Efficent / succinct solution example by Bradley Sward
    NB: Amended to use defaultdict
    """

    from collections import defaultdict

    with open(filename) as file:
        lines = file.readlines()

    splits = defaultdict(int)
    for l in lines:
        splits[l.index('S')] = 1
        break

    for l in lines[1:]:
        next = defaultdict(int)

        for split in splits:
            if l[split] == '^':
                next[split+1] += splits[split]
                next[split-1] += splits[split]
            else:
                next[split] += splits[split]
        splits = next

    return sum(splits.values())
