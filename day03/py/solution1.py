# day03; Part 1

import re
import os
from typing import List, Tuple
from collections import namedtuple

the_text: List[str] = []

Day3Match: Tuple[int, int, int] = namedtuple('Match', ['value', 'x', 'y'])

def parseMatches() -> List[Day3Match]:
    '''From 'the_text' variable'''
    matches: List[Day3Match] = []
    for line_index, line in enumerate(the_text):
        for part in re.finditer(r"[\d]+", line):
            # print(f"[DEBUG] Found match: {part}")
            matches.append(Day3Match(value=int(line[part.start():part.end()]), x=part.start(), y=line_index ))
    return matches

def filterForPartNumbers(a_match: Day3Match) -> bool:
    '''Search for surrounding parts in 'the_text'.'''
    line_length: int = len(the_text[0])
    lines_in_text: int = len(the_text)
    match_length: int = len(str(a_match.value))
    for x in range(max(0, a_match.x-1), min(line_length, a_match.x + match_length + 1)):
        for y in range (max(0,a_match.y-1), min(lines_in_text, a_match.y + 2)):
            if the_text[y][x] != '.' and not the_text[y][x].isdigit():
                print(f"[DEBUG] Found part for {a_match} @ ({x};{y})")
                return True
    return False

def solve(inputOfDay: str) -> str:
    global the_text
    the_text = inputOfDay.splitlines()
    matches: List[Day3Match] = parseMatches()
    print(f"Found matches: {matches}")
    filtered_matches = filter(filterForPartNumbers, matches)
    return str(sum([f_m.value for f_m in filtered_matches]))

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
    with open('../input/day03-1.input', 'r') as f:
        inputOfDay = f.read()
    test()
    print(solve(inputOfDay))
