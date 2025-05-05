def pl_resolution(kb):
    clauses = [set(clause) for clause in kb]
    new = set()

    while True:
        pairs = [(clauses[i], clauses[j])
                 for i in range(len(clauses))
                 for j in range(i + 1, len(clauses))]

        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            if frozenset() in resolvents:
                return True  # Contradiction found
            new.update(resolvents)

        if all(res in map(frozenset, clauses) for res in new):
            return False  # No new information

        for c in new:
            if set(c) not in clauses:
                clauses.append(set(c))


def resolve(ci, cj):
    resolvents = set()
    for literal in ci:
        if -literal in cj:
            resolvent = (ci - {literal}) | (cj - {-literal})
            resolvents.add(frozenset(resolvent))
    return resolvents



if __name__ == "__main__":
    cnf = [[1, -2, 3], [-1, 2], [3]]
    result = pl_resolution(cnf)

    if result:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
