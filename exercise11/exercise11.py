from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from collections import defaultdict

remove = set(stopwords.words("english")) | set(string.punctuation)

# input: file name
# output: word-context matrix
def wordContextMatrix(file_name):
    counts = defaultdict(lambda: defaultdict(int))

    with open(file_name) as f:
        for line in f:
            tokens = word_tokenize(line.lower())
            tokens = [t for t in tokens if t not in remove]
            for i, word in enumerate(tokens):
                # TODO: figure out why are we picking up extra context
                context = tokens[max(0, i-6):max(0, i)]
                context += tokens[i+1:i+6]
                for c in context:
                    counts[word][c] += 1

    # TODO: create matrix from counts
    return None

# input: a word-count matrix, first word, second word
# output: the cosine similarity between the two words
def cosine_similarity(matrix, w1, w2):
    # TODO: calculate cosine similarity
    return 0