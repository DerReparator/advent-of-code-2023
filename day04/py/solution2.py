# day04; Part 2

import os
from typing import List, Tuple, Set
from collections import namedtuple

Scratchcard = namedtuple('Scratchcard', ["winning", "numbers"])

def parse_scratchcard(line: str) -> Scratchcard:
    winning_numbers: Set[int] = set([int(nmbr) for nmbr in line.split(": ")[1].split(" | ")[0].split()])
    your_numbers: Set[int] = set([int(nmbr) for nmbr in line.split(": ")[1].split(" | ")[1].split()])
    return Scratchcard(winning=winning_numbers, numbers=your_numbers)

def calculate_points(scratchcard: Scratchcard) -> int:
    n: int = len((scratchcard.winning & scratchcard.numbers))
    if n == 0:
        return 0
    else:
        return 2**(n-1)

def solve(inputOfDay: str) -> str:
    scratchcards: List[Scratchcard] = [parse_scratchcard(line) for line in inputOfDay.splitlines()]
    return str(sum([calculate_points(sc) for sc in scratchcards]))

def test():
    test_cases: List[Tuple[str, str]] = []
    test_dir: str = "../input_test"
    for test_case_input in [os.path.join(test_dir, fname) for fname in os.listdir(test_dir)]:
        if test_case_input.endswith("2.input"):
            print(f"[DEBUG] Found test case input: {test_case_input}")
            test_case_expected = test_case_input.removesuffix("2.input") + "2.expected"
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
    with open('../input/day04-2.input', 'r') as f:
        inputOfDay = f.read()
    test()
    #print(solve(inputOfDay))
