def left_binarization(input_rules):
    """
     Input: A list of rules in the form ("SBAR", ["S", "NP", "VP"])
     Output: A list of rules ("SBAR", ["S-NP", "VP"]), ("S-NP", ["S", "NP"])
     """
    rules = []
    agenda = input_rules
    while(agenda):
        rule = agenda.pop()
        lhs = rule[0]
        rhs = rule[1]
        pr = rule[2]
        # If there's more than 2 symbols on the RHS, create a new rule
        if(len(rhs) > 2):
            joined_rule = "-".join(rhs[:-1])
            rules.append((lhs, [joined_rule, rhs[-1]], pr))
            agenda.append((joined_rule, rhs[:-1], 1))
        # Otherwise save it to the list of new rules
        else:
            rules.append(rule)
    
    # Remove duplicate rules
    rules.sort()
    rules = [rule for i, rule in enumerate(rules) if i==0 or rule != rules[i-1]]   
    return rules

def _test(rules):
    print rules
    print left_binarization(rules)
    
def test():
    rules = [
        ("NP", ["NP", "VP"], 0.5),
        ("SBAR", ["S", "NP", "VP"], 0.75),
        ("NP", ["DT", "JJ", "NN", "NN"], 0.5)
    ]
    print rules
    print "\nLeft binarization:"
    print left_binarization(rules)
    
if __name__ == '__main__':
    test()