from advent_2024.day_17.solutions import Computer

program = [2, 4, 1, 5, 7, 5, 4, 3, 1, 6, 0, 3, 5, 5, 3, 0]
expected = "2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0"

"""
A: ?
B: 0
C: 0

2,4 : A % 8 = B 
1,5 : B ^ 5 = B 
7,5 : A // 2**B = C
4,3 : B ^ C = B
1,6 : B ^ 6 => B
0,3 : A // 2**3 = A 
5,5 : out: B % 8
3,0 : start again

"""


starting_A = 24

computer = Computer(register_A=starting_A, register_B=0, register_C=0)
computer.run(program)
print(f"with A: {starting_A} output: {computer.output}")
if computer.output == expected:
    print(f"Success! A = {starting_A}")
