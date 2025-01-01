def solve_mod_equations():
    solutions = []

    # Check values of A from 0 to 100 (or another reasonable range)
    for A in range(10000):
        if (A // 8) % 8 == 0 and (A // 64) % 8 == 3:
            solutions.append(A)

    return solutions


# Get solutions
solutions = solve_mod_equations()
print("Possible values for A:", solutions)
