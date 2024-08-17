import time
import pathlib
import dataclasses
from dataclasses import dataclass
from collections import defaultdict


CARD_ORDER = "J 2 3 4 5 6 7 8 9 T Q K A"


@dataclass()
class BidHand:
    hand: str
    bid: int

    def __lt__(self, other):
        i = 0
        assert len(self.hand) == 5
        while i < 5 and CARD_ORDER.split().index(
            self.hand[i]
        ) == CARD_ORDER.split().index(other.hand[i]):
            i += 1
        if i == 5:
            return False
        if CARD_ORDER.split().index(self.hand[i]) < CARD_ORDER.split().index(
            other.hand[i]
        ):
            return True
        else:
            return False

    def get_type(self) -> int:
        unique_cards_per_hand = set(self.hand)
        if len(unique_cards_per_hand) == 1:
            return 7
        elif len(unique_cards_per_hand) == 4:
            return 2
        elif len(unique_cards_per_hand) == 5:
            return 1
        elif len(unique_cards_per_hand) == 2:
            counts = self._count_cards()
            if max(counts) == 4:
                return 6
            else:
                return 5
        elif len(unique_cards_per_hand) == 3:
            counts = self._count_cards()
            if max(counts) == 3:
                return 4
            else:
                return 3

    def _count_cards(self) -> list[int]:
        counts = list()
        for char in self.hand:
            counts.append(self.hand.count(char))
        return counts

    def get_type_with_jokers(self) -> str:
        trimmed_hand = self._remove_jokers(hand=self.hand)
        if len(trimmed_hand) == 0:
            return "JJJJJ"
        modal_card_in_trimmed = self._get_modal_card(hand=trimmed_hand)
        new_hand = ""
        for char in self.hand:
            if char != "J":
                new_hand += char
            else:
                new_hand += modal_card_in_trimmed
        return new_hand

    @staticmethod
    def _get_modal_card(hand: str) -> str:
        counts = list()
        for char in hand:
            counts.append((hand.count(char), char))
        highest_count = max(counts)
        return highest_count[1]

    @staticmethod
    def _remove_jokers(hand: str) -> str:
        trimmed_hand = ""
        for char in hand:
            if char != "J":
                trimmed_hand += char
        return trimmed_hand


def find_total_camel_card_winnings_with_jokers(file: str):
    bid_hands = _get_bid_hands(file=file)
    sorted_bid_hands_by_type = _get_sorted_bid_hands_by_type(bid_hands=bid_hands)
    return _get_total_winnings(sorted_bid_hands_by_type=sorted_bid_hands_by_type)


def _get_total_winnings(sorted_bid_hands_by_type: dict[int, list[BidHand]]) -> int:
    total = 0
    counter = 0
    for _, value in sorted_bid_hands_by_type.items():
        number_of_hands_in_type = len(value)
        for index in range(number_of_hands_in_type):
            total += (counter + index + 1) * value[index].bid
        counter += number_of_hands_in_type
    return total


def _get_sorted_bid_hands_by_type(
    bid_hands: list[BidHand],
) -> dict[int, list[BidHand]]:
    hands_by_type = defaultdict(list)
    for bid_hand in bid_hands:
        original_hand = bid_hand.hand
        new_hand = bid_hand.get_type_with_jokers()
        bid_hand = dataclasses.replace(bid_hand, hand=new_hand)
        type = bid_hand.get_type()
        bid_hand = dataclasses.replace(bid_hand, hand=original_hand)
        hands_by_type[type].append(bid_hand)
    sorted_hands_by_type = dict(sorted(hands_by_type.items()))
    for key, value in sorted_hands_by_type.items():
        sorted_hands_by_type[key] = sorted(value)
    return sorted_hands_by_type


def _get_bid_hands(file: str) -> list[BidHand]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        hands_with_rank = puzzle_input.readlines()
        bid_hands: list[BidHand] = list()
        for hand_with_rank in hands_with_rank:
            hand = hand_with_rank.split()[0]
            rank = int(hand_with_rank.split()[1])
            bid_hands.append(BidHand(hand=hand, bid=rank))
    return bid_hands


start = time.perf_counter()
print(find_total_camel_card_winnings_with_jokers("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
print(find_total_camel_card_winnings_with_jokers("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
