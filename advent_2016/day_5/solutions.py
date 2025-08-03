from pathlib import Path
import hashlib
from reusables import timer, INPUT_PATH


def _read_input(file_path: Path):
    with open(file_path, "r") as puzzle_input:
        return puzzle_input.read().strip()


@timer
def part_one(file: str, day: int = 5, year: int = 2016) -> str:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    door_id = _read_input(file_path=input_file_path)
    i = 1
    password = ""
    while len(password) <= 8:
        i += 1
        test_string = door_id + str(i)
        hsh = hashlib.md5(string=test_string.encode())
        res = hsh.hexdigest()
        if res[:5] == "00000":
            # print(res)
            password += str(res[5])
    return password


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 5, year: int = 2016) -> str:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    door_id = _read_input(file_path=input_file_path)
    i = 1
    password = {n: "" for n in range(8)}
    while any(val == "" for val in password.values()):
        i += 1
        test_string = door_id + str(i)
        hsh = hashlib.md5(string=test_string.encode())
        res = hsh.hexdigest()
        if res[:5] == "00000":
            # print(res)
            position = res[5]
            if not position.isnumeric():
                continue
            position_i = int(position)
            if position_i <= 7:
                # print(password)
                if password[position_i] == "":
                    password[position_i] = res[6]
    return "".join([password[i] for i in range(8)])


part_two(file="eg")
part_two(file="input")
