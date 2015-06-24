from __future__ import division
from probabilistic_cnf import left_binarization
from probabilistic_cyk import parse

def read_rules(file):
    rules = []
    current_lhs = None
    current_lhs_rules = []
    current_lhs_count = 0
    with open(file, 'r') as rules_file:
        for line in rules_file:
            columns = line.split()
            count = int(columns[0])
            lhs = columns[1]
            rhs = columns[2:]
            if lhs != current_lhs:
                for rule in current_lhs_rules:
                    rules.append((rule[0], rule[1], rule[2]/current_lhs_count))
                current_lhs = lhs
                current_lhs_rules = []
                current_lhs_count = 0
            current_lhs_rules.append((lhs, rhs, count))
            current_lhs_count += count
    return rules

grammar = read_rules("rules.txt")
lexicon = read_rules("lexicon.txt")

grammar = left_binarization(grammar) + (lexicon)

print parse(grammar, "The reason was not high interest rates or labor costs".split())
print parse(grammar, "Many other factors played a part in yesterday 's comeback".split())