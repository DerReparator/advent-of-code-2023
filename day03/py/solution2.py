# day03; Part 2

import re
import os
from typing import List, Tuple, Dict
from collections import namedtuple, defaultdict
import math

the_text: List[str] = []
matched_gears: Dict[Tuple[int, int], List[int]] = defaultdict(list)

Day3Match: Tuple[int, int, int] = namedtuple('Match', ['value', 'x', 'y'])

def parseMatches() -> List[Day3Match]:
    '''From 'the_text' variable'''
    matches: List[Day3Match] = []
    for line_index, line in enumerate(the_text):
        for part in re.finditer(r"[\d]+", line):
            # print(f"[DEBUG] Found match: {part}")
            matches.append(Day3Match(value=int(line[part.start():part.end()]), x=part.start(), y=line_index ))
    return matches

def filterForGearPartNumbers(a_match: Day3Match) -> bool:
    '''Search for surrounding parts in 'the_text'.'''
    global the_text, matched_gears
    line_length: int = len(the_text[0])
    lines_in_text: int = len(the_text)
    match_length: int = len(str(a_match.value))
    for x in range(max(0, a_match.x-1), min(line_length, a_match.x + match_length + 1)):
        for y in range (max(0,a_match.y-1), min(lines_in_text, a_match.y + 2)):
            if the_text[y][x] == '*':
                coords:Tuple[int,int] = (x,y)
                matched_gears[coords].append(a_match.value)
                print(f"[DEBUG] Found gear for {a_match} @ ({x};{y})")
                return True
    return False

def solve(inputOfDay: str) -> str:
    global the_text, matched_gears
    the_text = inputOfDay.splitlines()
    matches: List[Day3Match] = parseMatches()
    print(f"Found matches: {matches}")
    filtered_matches = list(filter(filterForGearPartNumbers, matches))
    print(f"Filtered Parts: {filtered_matches}")
    for _, parts in matched_gears:
        print(f"[DEBUG] Parts: {parts}")
    return str(sum([math.prod(parts) for parts in matched_gears.values() if len(parts) == 2]))

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
    with open('../input/day03-2.input', 'r') as f:
        inputOfDay = f.read()
    #test()
    print(solve(inputOfDay))
