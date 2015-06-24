
from collections import defaultdict
from reader import Reader

def train(filename):
    femit = defaultdict(lambda: defaultdict(int))
    ftrans = defaultdict(lambda: defaultdict(int))
    with open(filename) as f:
        for i, sent in enumerate(Reader(f)):
            sent = [('', 'START')] + sent + [('', 'END')]
            for (word, pos) in sent:
                femit[pos][word] += 1
            for i, (word, pos) in enumerate(sent[1:]):
                ftrans[sent[i][1]][pos] += 1
    return femit, ftrans
