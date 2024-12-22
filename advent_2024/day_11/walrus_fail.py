from typing import Optional

print("example 1 -------------------------------")
results = []
for x in range(10):
    y = x**2
    if y > 10:
        results.append(y)
print(f"results 1: {results}")

results = [y for x in range(10) if (y := x**2) > 10]
print(f"results 2: {results}")

print("example 2 -----------------------------")
lines = ["start", "run", "stop"]
i = 0
while lines[i] != "stop":
    print(lines[i])
    i += 1

i = 0
while (line := lines[i]) != "stop":
    print(line)
    i += 1

print("example 3 -------------------------------")


def _compute():
    return 11


value = _compute()
if value > 10:
    print(f"Value is too high: {value}")

if (value := _compute()) > 10:
    print(f"Value is too high: {value}")


print("example 4 ------------------------------")


def split(n: int) -> Optional[list[int]]:
    s = str(n)
    if len(s) % 2 == 0:
        return [int(s[: len(s) // 2]), int(s[len(s) // 2 :])]
    return None


def apply_rules(n: int) -> list[int]:
    if n == 0:
        return [1]
    if (splitted := split(n)) is not None:
        return splitted
    return [n * 2024]


def apply_rules_a(n: int) -> list[int]:
    if n == 0:
        return [1]
    elif split(n) is not None:
        return split(n)
    return [n * 2024]


print(f"{apply_rules(55)}")
print(f"{apply_rules_a(55)}")
