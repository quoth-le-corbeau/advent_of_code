from pathlib import Path
import re
from dataclasses import dataclass

from reusables import timer, INPUT_PATH


@dataclass(frozen=True)
class IpAddress:
    hypernets: list[str]
    supernets: list[str]

    def assert_reconstructed(self, ip_line: str):
        reconstructed = ""
        assert len(self.hypernets) == len(self.supernets) - 1
        for i in range(len(self.hypernets)):
            reconstructed += self.supernets[i] + "[" + self.hypernets[i] + "]"
        reconstructed += self.supernets[-1]
        assert reconstructed == ip_line

    def supports_tls(self) -> bool:
        return not self._abba_in_hypernets() and self._abba_in_supernets()

    def _abba_in_hypernets(self) -> bool:
        return any(_has_abba_re(string_=hypernet) for hypernet in self.hypernets)

    def _abba_in_supernets(self) -> bool:
        return any(_has_abba_re(string_=supernet) for supernet in self.supernets)


def _parse_ips(file_path: Path) -> list[IpAddress]:
    with open(file_path, "r") as puzzle_input:
        hypernet_pattern = r"\[(.*?)\]"
        ip_addresses = []
        for ip_line in puzzle_input.read().strip().splitlines():
            hypernets = re.findall(pattern=hypernet_pattern, string=ip_line)
            supernets = list(
                filter(
                    lambda s: s not in hypernets,
                    re.split(pattern=hypernet_pattern, string=ip_line),
                )
            )
            ip_address = IpAddress(supernets=supernets, hypernets=hypernets)
            ip_address.assert_reconstructed(ip_line)
            ip_addresses.append(ip_address)
        return ip_addresses


def _has_abba_re(string_: str) -> bool:
    pattern = r"(?=(([a-zA-Z])(?!\2)([a-zA-Z])\3\2))"
    matches = [m.group(1) for m in re.finditer(pattern, string_)]
    return len(matches) == 1


def _has_abba_me(string_: str) -> bool:
    """re is faster than me ;-)"""
    for i in range(len(string_) - 3):
        to_examine = string_[i : i + 4]
        if to_examine[:2] == to_examine[-2:][::-1] and len(set(to_examine)) == 2:
            return True
    return False


@timer
def part_one(file: str, day: int = 7, year: int = 2016) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    ip_addresses = _parse_ips(file_path=input_file_path)
    count = 0
    for ip_address in ip_addresses:
        if ip_address.supports_tls():
            count += 1
    return count


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2016):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )


part_two(file="eg")
part_two(file="input")
