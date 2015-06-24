from collections import defaultdict

def parse(grammar, sent):
    probs = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
    trees = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    non_terminals = [rule for rule in grammar if len(rule[1]) > 1]
    terminals = [rule for rule in grammar if len(rule[1]) == 1]
    for i in range(len(sent)):
        for rule in terminals:
            if sent[i] == rule[1][0]:
                # note: the indices were modified from the original algorithm
                #       to make dealing with zero-indexing easier
                probs[i][i][rule[0]] = rule[2]
                trees[i][i][rule[0]] = [rule[0], sent[i]]
        # for j from i-2...0
        for j in range(max(i-1, -1), -1, -1):
            for k in range(j, i):
                for rule in non_terminals:
                    a = rule[0]
                    b = rule[1][0]
                    c = rule[1][1]
                    pr = probs[j][k][b] * probs[k+1][i][c] * rule[2]
                    if(pr > probs[j][i][a]):
                        probs[j][i][a] = pr
                        trees[j][i][a] = [a, trees[j][k][b], trees[k+1][i][c]]
    return (trees[0][len(sent) - 1]["S"], probs[0][len(sent) - 1]["S"])


grammar = [
    ("S", ["NP", "VP"], 1.0),
    ("NP", ["DET", "N"], 0.8),
    ("NP", ["NP", "PP"], 0.2),
    ("VP", ["V", "NP"], 0.4),
    ("VP", ["VP", "PP"], 0.6),
    ("PP", ["P", "NP"], 1.0),
    ("DET", ["a"], 0.2),
    ("DET", ["the"], 0.8),
    ("N", ["student"], 0.55),
    ("N", ["book"], 0.25),
    ("N", ["library"], 0.2),
    ("V", ["reads"], 1.0),
    ("P", ["in"], 1.0)
]

def _test(sent):
    print sent
    print parse(grammar, sent)
    
def test():
    _test("the student reads a book in the library".split())
    _test("the student reads a book".split())
    _test("the student reads in the library".split())

if __name__ == '__main__':
    test()
    