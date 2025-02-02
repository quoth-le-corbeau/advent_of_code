from advent_2024.day_17.solutions_old import ChronospatialComputer
from reusables import dict_parametrize


@dict_parametrize(
    {
        "_bxl": {
            "registers": (0, 29, 0),
            "program": [1, 7],
            "expected_registers": (0, 26, 0),
            "expected_output": "",
        },
        "_bst": {
            "registers": (0, 0, 9),
            "program": [2, 6],
            "expected_registers": (0, 1, 9),
            "expected_output": "",
        },
        "_out": {
            "registers": (10, 0, 0),
            "program": [5, 0, 5, 1, 5, 4],
            "expected_registers": (10, 0, 0),
            "expected_output": "0,1,2",
        },
        "_adv_out_jnz": {
            "registers": (2024, 0, 0),
            "program": [0, 1, 5, 4, 3, 0],
            "expected_registers": (0, 0, 0),
            "expected_output": "4,2,5,6,7,7,7,7,3,1,0",
        },
        "_bxc": {
            "registers": (0, 2024, 43690),
            "program": [4, 0],
            "expected_registers": (0, 44354, 43690),
            "expected_output": "",
        },
    }
)
def test_computer(registers, program, expected_registers, expected_output):
    computer = ChronospatialComputer(
        register_A=registers[0],
        register_B=registers[1],
        register_C=registers[2],
    )
    output = computer.run(program)
    assert output == expected_output
    assert (
        computer.register_A,
        computer.register_B,
        computer.register_C,
    ) == expected_registers
