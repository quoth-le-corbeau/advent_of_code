def gcd_two(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd_two(b % a, a)


def lcm_two(a: int, b: int) -> int:
    return int(a * b / gcd_two(a, b))


def lcm_many(integers: list[int]) -> int:
    lcm = 1
    for integer in integers:
        lcm = lcm_two(lcm, integer)
    return lcm


test_list = [4, 6, 8, 12, 16]
print(lcm_many(test_list))


def verify_modulo_divisibility(dividend: int, divisors: list[int]):
    remainder_lcm = dividend % lcm_many(divisors)
    for x in divisors:
        assert dividend % x == remainder_lcm % x
    return remainder_lcm


print(verify_modulo_divisibility(dividend=144, divisors=test_list))
print(verify_modulo_divisibility(dividend=145, divisors=test_list))
print(verify_modulo_divisibility(dividend=21187, divisors=test_list))
