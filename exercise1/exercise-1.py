# Computational Linguistics - Assignment #1
# Stephanie Lund (2555914), Laura Fraedrich (2556722), Francesco Tombini (2554549)
# To run: "python exercise-1.py"

from collections import defaultdict

class NFA:
    
    # k is the set of states
    # sigma is the alphabet
    # delta is a 2-dimensional array where the first key is the state
    #    , the second key is a single character, and the values are sets of states
    # s is the start state
    # f is the set of final states
    def __init__(self, k, sigma, delta, s, f):
        self.k = k
        self.sigma = sigma
        self.delta = delta
        self.s = s
        self.f = f

class DFA:
    # delta is a 2-dimensional array where the first key is the state
    #    , the second key is a single character, and the values are single states
    def __init__(self, k, sigma, delta, s, f):
        self.k = k
        self.sigma = sigma
        self.delta = delta
        self.s = s
        self.f = f
    
    def __str__(self):
        output = "DFA with states: {0}\n".format(self.k)
        output += "alphabet: {0}\n".format(self.sigma)
        output += "transition function: \n"
        for state in self.delta.keys():
            for a in self.delta[state].keys():
                output += "d({0}, {1}) = {2})\n".format(list(state), a, list(self.delta[state][a]))
        output += "start state: {0}\n".format(list(self.s))
        output += "final states: "
        output += ", ".join([str(list(state)) for state in self.f])
        return output

# Exercise 3 : Recognition algorithm for NFAs
def recognize(m, inpt):
    agenda = [(m.s, inpt)]
    while agenda:
        (state, string) = agenda.pop()
        if len(string) == 0 and state in m.f:
            return True
        else:
            if len(string) > 0:
                for k in m.delta[state][string[0]]:
                    new_conf = (k, string[1:])
                    agenda.append(new_conf)
            # epsilon transitions
            for k in m.delta[state][""]:
                new_conf = (k, string)
                agenda.append(new_conf)
    return False
    
    
# Exercise 4 : Subset algorithm
def dfa(m):
    unmarked = [epsilon_closure(m, [m.s])]
    marked = []
    delta = defaultdict(lambda: defaultdict(set))
    
    while len(unmarked) > 0:
        t = unmarked.pop()
        marked.append(t)
        for a in m.sigma:
            u = set()
            for state in t:
                u.update(epsilon_closure(m, m.delta[state][a]))
            u = frozenset(u)
            if not u in (unmarked + marked):
                unmarked.append(u)
            delta[t][a] = u
    
    f = set()
    for state in marked:
        if len(state & m.f) > 0:
            f.add(state)
    
    return DFA(m.k, m.sigma, delta, epsilon_closure(m, [m.s]), f)

# return the epsilon closure of set of states s in m
def epsilon_closure(m, s):
    e = set(s)
    size = 0
    while size != len(e):
        size = len(e)
        for state in e:
            e.update(m.delta[state][""])
    return frozenset(e)


# Tests
delta = defaultdict(lambda: defaultdict(set))
delta[0]["a"].add(1)
delta[1]["b"].update([2,3])
delta[2]["a"].add(1)
delta[3]["a"].add(2)


m = NFA([0,1,2,3], ["a", "b"], delta, 0, set([0, 2]))

strings = ["ab", "aba", "abaab", "abba", "aabab"]

print "Exercise 3: \n"
for s in strings:
    result = recognize(m, s)
    print "{0}: {1}\n".format(s, result)

print "Exercise 4: \n"
print dfa(m)