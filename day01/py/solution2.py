# day01; Part 2

import os
from typing import List, Tuple
import re

number_strings = [
("one", "1"),
        ("two",     "2"),
        ("three",   "3"),
        ("four",    "4"),
        ("five",    "5"),
        ("six",     "6"),
        ("seven",   "7"),
        ("eight",   "8"),
        ("nine",    "9")
]

def solve(inputOfDay: str) -> str:
    calibration: int = 0
    for line in inputOfDay.splitlines():
        # find first digit
        first_digit = "0"
        for i in range(len(line)):
            tmp_line = line[i:]
            for number_string in number_strings:
                tmp2_line = tmp_line.replace(number_string[0], number_string[1])
                if len(re.findall(r'^\d', tmp2_line)) > 0:
                    first_digit = tmp2_line[0]
                    break
            if first_digit != "0":
                break
        
        #find last digit
        last_digit = "0"
        for i in range(0, len(line)):
            if i == 0:
                tmp_line = line
            else:
                tmp_line = line[:-i]
            for number_string in number_strings:
                tmp2_line = tmp_line.replace(number_string[0], number_string[1])
                if len(re.findall(r'\d$', tmp2_line)) > 0:
                    last_digit = tmp2_line[-1]
                    break
            if last_digit != "0":
                break
        
        calibration_val = int(f"{first_digit}{last_digit}")
        print(calibration_val)
        calibration += calibration_val
    return str(calibration)

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
    with open('../input/day01-2.input', 'r') as f:
        inputOfDay = f.read()
    #test()
    print(solve(inputOfDay))
