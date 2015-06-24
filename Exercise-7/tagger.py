
import sys

from reader import Reader
from train import train
from hmm import HMM

def main():
    hmm = HMM(*train(sys.argv[1]))
    
    with open(sys.argv[2]) as f:
        correct = 0
        wrong = 0
        
        correct_sents = 0
        wrong_sents = 0
        
        correct_known = 0
        wrong_known = 0
        
        for i, sent in enumerate(Reader(f)):
            prob, path = hmm.decode([word for (word, pos) in sent])
            correct1 = 0
            wrong1 = 0
            for (gold, predicted) in zip(sent, path):
                if gold == predicted:
                    correct1 += 1
                else:
                    wrong1 += 1
            print('%e\t%.3f\t%s' % (prob, correct1 / (correct1 + wrong1), ' '.join('%s/%s' % pair for pair in path)))
            if prob > 0:
                correct_sents += 1
                correct_known += correct1
                wrong_known += wrong1
            else:
                wrong_sents += 1
            correct += correct1
            wrong += wrong1
    
    print("Correctly tagged words: %s" % (correct / (correct + wrong)))
    print("Sentences with non-zero probability: %s" % (correct_sents / (correct_sents + wrong_sents)))
    print("Correctly tagged words when only considering sentences with non-zero probability: %s" % (correct_known / (correct_known + wrong_known)))

if __name__ == '__main__':
    main()
