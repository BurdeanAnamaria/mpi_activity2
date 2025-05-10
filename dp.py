from copy import deepcopy

def is_pure_literal(clauses, literal):
    has_pos = any(literal in clause for clause in clauses)
    has_neg = any(-literal in clause for clause in clauses)
    if has_pos and not has_neg:
        return True, True
    elif has_neg and not has_pos:
        return True, False
    return False, None

def unit_propagate(clauses, assignment):
    unit_clauses = [c for c in clauses if len(c) == 1]
    while unit_clauses:
        unit = unit_clauses[0][0]
        assignment[abs(unit)] = unit > 0
        clauses = simplify(clauses, unit)
        if [] in clauses:
            return None, None
        unit_clauses = [c for c in clauses if len(c) == 1]
    return clauses, assignment

def simplify(clauses, literal):
    new_clauses = []
    for clause in clauses:
        if literal in clause:
            continue
        if -literal in clause:
            new_clause = [x for x in clause if x != -literal]
            new_clauses.append(new_clause)
        else:
            new_clauses.append(clause)
    return new_clauses

def dp(clauses, assignment):
    clauses, assignment = unit_propagate(clauses, assignment)
    if clauses is None:
        return None
    if not clauses:
        return assignment

    literals = set(abs(l) for clause in clauses for l in clause)
    for l in literals:
        if l not in assignment:
            break

    new_assignment = assignment.copy()
    new_assignment[l] = True
    simplified = simplify(clauses, l)
    result = dp(simplified, new_assignment)
    if result is not None:
        return result

    new_assignment = assignment.copy()
    new_assignment[l] = False
    simplified = simplify(clauses, -l)
    return dp(simplified, new_assignment)


if __name__ == "__main__":
    cnf = [[1, -2, 3], [-1, 2], [3]]  
    solution = dp(cnf, {})
    if solution:
        print("SATISFIABLE")
        for var in sorted(solution):
            print(f"x{var} = {solution[var]}")
    else:
        print("UNSATISFIABLE")
