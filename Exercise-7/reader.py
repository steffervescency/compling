
class Reader:
    def __init__(self, it):
        self._it = it
    def __iter__(self):
        return self
    def __next__(self):
        lines = []
        for line in self._it:
            if line.isspace():
                break
            lines.append(tuple(line.strip().split('\t')))
        else:
            raise StopIteration
        return lines

if __name__ == '__main__':
    import sys
    for sentence in Reader(sys.stdin):
        print(sentence)

