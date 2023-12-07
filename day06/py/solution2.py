# day06; Part 2

import os
from typing import List, Tuple
from collections import namedtuple
import re

PastRace = namedtuple("PastRace", ["time", "recordDistance"])

def parse_races(input_of_day: str) -> List[PastRace]:
    time_str: str = input_of_day.splitlines()[0].split(':')[1].replace(" ", "")
    distance_str: str = input_of_day.splitlines()[1].split(':')[1].replace(" ", "")

    yield PastRace(int(time_str), int(distance_str))

# d(t_pressed)  = t_pressed * (t_race - t_pressed)
# [mm]          = [mm/s] * ([s] - [s])

def calculate_no_of_winning_milliseconds(race: PastRace) -> int:
    min_t_pressed: int = race.time
    max_t_pressed: int = 0

    for t_pressed in range(race.time):
        if t_pressed * (race.time - t_pressed) > race.recordDistance:
            min_t_pressed = t_pressed
            break

    for t_pressed in range(race.time, 0, -1):
        if t_pressed * (race.time - t_pressed) > race.recordDistance:
            max_t_pressed = t_pressed
            break
    return max_t_pressed - min_t_pressed + 1

def solve(inputOfDay: str) -> str:
    solution: int = 1
    for race in parse_races(inputOfDay):
        solution = solution * calculate_no_of_winning_milliseconds(race)
    return str(solution)

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
    with open('../input/day06-2.input', 'r') as f:
        inputOfDay = f.read()
    #test()
    print(solve(inputOfDay))
