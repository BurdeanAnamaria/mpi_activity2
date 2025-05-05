# SAT Solver
This is a simple SAT solver implementation in Python using:
- Resolution
- Davis-Putnam (DP)
- Davis-Putnam-Logemann-Loveland (DPLL)

## Usage
Each algorithm is in its own file:
- `resolution.py`
- `dp.py`
- `dpll.py`

CNF formulas are represented as lists of clauses:
```python
cnf = [[1, -2, 3], [-1, 2], [3]]
```
