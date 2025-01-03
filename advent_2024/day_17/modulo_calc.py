from tqdm import tqdm

# ROUND 1 of 16 -----------
# s0 registers: A: a, B: 0, C: 0
# s1 (2, 4) reg: A: a, B: a % 8, C: 0
# s2 (1, 5) reg: A: a, B: (a % 8) ^ 5 C: 0
# s3 (7, 5) reg: A: a, B: (a % 8) ^ 5, C: a // ((a % 8) ^ 5)
# s4 (4, 3) reg: A: a, B: ((a % 8) ^ 5) ^ (a // ((a % 8) ^ 5)), C: a // ((a % 8) ^ 5)
# s5 (1, 6) reg: A: a, B: ((a % 8) ^ 5) ^ (a // ((a % 8) ^ 5)) ^ 6, C: a // ((a % 8) ^ 5)
# s6 (0, 3) reg: A: a // 2**3, B: ((a % 8) ^ 5) ^ (a // ((a % 8) ^ 5)) ^ 6, C: a // ((a % 8) ^ 5)
# s7 (5, 5) reg: A: a // 2**3, B: ((a % 8) ^ 5) ^ (a // ((a % 8) ^ 5)) ^ 6, C: a // ((a % 8) ^ 5)
#   -> out: (((a % 8) ^ 5) ^ (a // ((a % 8) ^ 5)) ^ 6) % 8 = 2
# s8 (3, 0), a > 0 so reset to start
# ROUND 2 of 16 -----------
# s1 (2, 4) reg: A: a // 2**3, B: (a // 2**3) % 8, C: a // ((a % 8) ^ 5)
# s2 (1, 5) reg: A: a // 2**3, B: ((a // 2**3) % 8) ^ 5, C: a // ((a % 8) ^ 5)
# s3 (7, 5) reg: A: a // 2**3, B: ((a // 2**3) % 8) ^ 5, C: (a // (2**3)) // (((a // 2**3) % 8) ^ 5)
# s4 (4, 3) reg: A: a // 2**3, B: (((a // 2**3) % 8) ^ 5) ^ ((a // (2**3)) // (((a // 2**3) % 8) ^ 5)), C: (a // (2**3)) // (((a // 2**3) % 8) ^ 5)
# s5 (1, 6) reg: A: a // 2**3, B: ((((a // 2**3) % 8) ^ 5) ^ ((a // (2**3)) // (((a // 2**3) % 8) ^ 5))) ^ 6, C: (a // (2**3)) // (((a // 2**3) % 8) ^ 5)
# s6 (0, 3) reg: A: a // 2**6, B: ((((a // 2**3) % 8) ^ 5) ^ ((a // (2**3)) // (((a // 2**3) % 8) ^ 5))) ^ 6, C: (a // (2**3)) // (((a // 2**3) % 8) ^ 5)
# s7 (5, 5) reg: A: a // 2**6, B: ((((a // 2**3) % 8) ^ 5) ^ ((a // (2**3)) // (((a // 2**3) % 8) ^ 5))) ^ 6, C: (a // (2**3)) // (((a // 2**3) % 8) ^ 5)
#    -> out: (((((a // 2**3) % 8) ^ 5) ^ ((a // (2**3)) // (((a // 2**3) % 8) ^ 5))) ^ 6) % 8 = 4
# s8 (3, 0), reset


def part_two_composite():
    program = [2, 4, 1, 5, 7, 5, 4, 3, 1, 6, 0, 3, 5, 5, 3, 0]
    solutions = []
    # Define the total iterations in the loop
    total_iterations = 2**46
    # Wrap the loop with tqdm to display progress
    for a in tqdm(
        range(total_iterations - 1000000000, total_iterations - 1000000000000, -1),
        desc="Processing",
        ncols=100,
    ):
        try:
            if (
                (((a // 2**45) % 8) ^ 5)
                ^ ((a // 2**45) // (((a // 2**45) % 8) ^ 5))
                ^ 6
            ) % 8 == 0:
                solutions.append(a)
                print(a)
        except ZeroDivisionError:
            # print(f"zero division error at a={a} which is the {a - 2**45}")
            continue
    return solutions


print(f"possible values for A: {part_two_composite()}")

# 35184372088833 two low
