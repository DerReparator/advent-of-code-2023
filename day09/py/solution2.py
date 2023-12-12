# day09; Part 2

import os
from typing import List, Tuple

def parse_history(history_str: str) -> List[int]:
    history = [int(value) for value in history_str.split()]
    history.reverse()
    return history

def solve(inputOfDay: str) -> str:
    solution: int = 0
    for history in [parse_history(s) for s in inputOfDay.splitlines()]:
        solution = solution + extrapolate_history(history)[-1]
    return str(solution)

def extrapolate_history(history: List[int]) -> List[int]:
    next_history: List[int] = []
    is_all_zeroes = history[0] == 0
    for i in range(len(history) - 1):
        if history[i + 1] != 0:
            is_all_zeroes = False
        next_history.append(history[i + 1] - history[i])
    if is_all_zeroes:
        history.append(0)
    else:
        history.append(extrapolate_history(next_history)[-1] + history[-1])
    return history

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
    with open('../input/day09-2.input', 'r') as f:
        inputOfDay = f.read()
    #test()
    print(solve(inputOfDay))
