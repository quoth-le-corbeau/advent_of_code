from pathlib import Path

from reusables import timer, INPUT_PATH


class CrossedWires:
    def __init__(self, file: str):
        self.ops = {
            "XOR": lambda x, y: 1 if x != y else 0,
            "OR": lambda x, y: 1 if x == 1 or y == 1 else 0,
            "AND": lambda x, y: 1 if x == 1 and y == 1 else 0,
        }
        with open(
            file=Path(__file__).resolve().parents[2] / file, mode="r"
        ) as puzzle_input:
            wire_lines, gate_inputs = puzzle_input.read().strip().split("\n\n")
            self.inputs_by_wire = {}
            for wire_line in wire_lines.splitlines():
                self.inputs_by_wire[wire_line.strip().split(": ")[0]] = int(
                    wire_line.strip().split(": ")[1]
                )
            self.gate_ops_by_output = {}
            for gate_input in gate_inputs.splitlines():
                wires_in, out = gate_input.strip().split(" -> ")
                self.gate_ops_by_output[out] = wires_in

    def evaluate(self):
        results_by_wire = {}
        while len(results_by_wire) != len(self.gate_ops_by_output):
            for wire, op in self.gate_ops_by_output.items():
                wire_1, func, wire_2 = op.split(" ")
                if wire_1 in self.inputs_by_wire and wire_2 in self.inputs_by_wire:
                    x, y = self.inputs_by_wire[wire_1], self.inputs_by_wire[wire_2]
                    results_by_wire[wire] = self.ops[func](x, y)
        return self.convert(results_by_wire)

    def convert(self, results_by_wire: dict[str, int]) -> int:
        targets = self.filter_z(results_by_wire)
        result = 0
        for i, target in enumerate(targets):
            _, value = target
            if value == 1:
                result += 2**i
        return result

    def filter_z(self, results_by_wire: dict[str, int]) -> list[tuple[str, int]]:
        targets = []
        for wire, value in results_by_wire.items():
            if wire[0] == "z":
                targets.append((wire, value))
        return sorted(targets)


@timer
def part_one(file: str, year: int = 2024, day: int = 24):
    input_file = INPUT_PATH.format(file=file, year=year, day=day)
    crossed_wires = CrossedWires(file=input_file)
    results_by_wire = crossed_wires.evaluate()
    print(results_by_wire)


part_one("eg")
part_one("eg2")
# part_one("input")
