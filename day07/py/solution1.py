# day07; Part 1

import os
from typing import List, Tuple
from enum import IntEnum
from functools import total_ordering
import re

# Five of a kind
# Four of a kind
# Full house
# Three of a kind
# Two pair
# One pair
# High card

class HandType(IntEnum):
    HIGH_CARD = 1,
    ONE_PAIR = 2,
    TWO_PAIR = 3,
    THREE_KIND = 4,
    FULL_HOUSE = 5,
    FOUR_KIND = 6,
    FIVE_KIND = 7

@total_ordering
class HandBid:
    def __init__(self, hand: str, bid: int) -> None:
        self.hand = hand
        self.bid = bid
        self.hand_type = self.parse_hand_type(hand)

    def parse_hand_type(self, hand: str) -> HandType:
        hand = ''.join(sorted(hand))
        if re.match(r"([AKQJT98765432])\1{4}", hand):
            return HandType.FIVE_KIND
        if re.search(r"([AKQJT98765432])\1{3}", hand):
            return HandType.FOUR_KIND
        if re.search(r"^([AKQJT98765432])\1{1,2}([AKQJT98765432])\2{1,2}$", hand):
            return HandType.FULL_HOUSE
        if re.search(r"([AKQJT98765432])\1{2}", hand):
            return HandType.THREE_KIND
        two_pair_result = re.findall(r"([AKQJT98765432])\1{1}", hand)
        if two_pair_result:
            if len(two_pair_result) == 2:
                return HandType.TWO_PAIR
            else:
                return HandType.ONE_PAIR
        # if re.search(r"([AKQJT98765432])\1{1}", hand):
        #     return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    def calculate_winning(self, rank: int) -> int:
        return self.bid * rank
    
    def card_is_lower(self, card_a: str, card_b: str) -> bool:
        cards = "23456789TJQKA"
        return cards.index(card_a) < cards.index(card_b)

    def __lt__(self, other):
        if other.hand_type == self.hand_type:
            for my_card, other_card in zip(self.hand, other.hand):
                if my_card == other_card:
                    continue
                return self.card_is_lower(my_card, other_card)
        return self.hand_type < other.hand_type
    
    def __eq__(self, __value: object) -> bool:
        # very naive implementation that assumes that '__value' is always of type HandBid
        return self.hand == __value.hand
    
    def __repr__(self) -> str:
        return f"{self.hand} ({self.hand_type.name}) bids {self.bid}"

def parse_hand_bit(input_str: str) -> HandBid:
    return HandBid(input_str.split()[0], int(input_str.split()[1]))

def solve(inputOfDay: str) -> str:
    hands: List[HandBid] = [parse_hand_bit(h) for h in inputOfDay.splitlines()]
    winnings: int = 0
    for rank, hand in enumerate(sorted(hands), start=1):
        print(f"[DEBUG] {rank}: {hand}")
        winnings = winnings + rank * hand.bid
    return str(winnings)


def test():
    test_cases: List[Tuple[str, str]] = []
    test_dir: str = "../input_test"
    for test_case_input in [os.path.join(test_dir, fname) for fname in os.listdir(test_dir)]:
        if test_case_input.endswith("1.input"):
            print(f"[DEBUG] Found test case input: {test_case_input}")
            test_case_expected = test_case_input.removesuffix("1.input") + "1.expected"
            print(f"[DEBUG] Searching test case expected at: {test_case_expected}")
            if not os.path.exists(test_case_expected):
                print(f"[WARN] Found no expected file for test case '{test_case_input}'")
                continue
            else:
                test_cases.append((test_case_input, test_case_expected))
    print(f"[INFO] Found {len(test_cases)} test cases.")
    for test_case in test_cases:
        execute_test(test_case)

def execute_test(test_files: Tuple[str, str]):
    input = ""
    with open(test_files[0], 'r') as input_file:
        input = input_file.read()
    test_result = solve(input)
    expected: str = ""
    with open(test_files[1], 'r') as expected_file:
        expected = expected_file.read()
    if (test_result == expected.strip()):
        print("[SUCCESS]")
    else:
        print(f"[FAIL]: Expected '{expected}'")
        print(f"Got: '{test_result}'")

if __name__=='__main__':
    # change working dir to script location
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    inputOfDay = ''
    with open('../input/day07-1.input', 'r') as f:
        inputOfDay = f.read()
    #test()
    print(solve(inputOfDay))
