
def implies(p, q):
    return (not p) or q


def kb(m):
    return implies(m['P'], m['Q']) and m['P']


def query(m):
    return m['Q']


def check_all(kb, query, symbols, model):

    if len(symbols) == 0:
        if kb(model):
            return query(model)
        else:
            return True

    p = symbols[0]
    rest = symbols[1:]

    m1 = model.copy()
    m1[p] = True

    m2 = model.copy()
    m2[p] = False

    return (check_all(kb, query, rest, m1)
            and check_all(kb, query, rest, m2))


symbols = ['P', 'Q']

result = check_all(kb, query, symbols, {})

print("Knowledge Base: P -> Q and P")
print("Query: Q")
print("Checking all possible models")

if result:
    print("Result: True")
    print("KB entails the query")
else:
    print("Result: False")
    print("KB does not entail the query")
