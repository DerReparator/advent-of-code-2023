# day05; Part 2

import math
import os
from typing import List, Tuple
from datetime import datetime

class Mapping:
    def __init__(self) -> None:
        self.raw_mappings: List[Tuple[int,int,int]] = []
        self.mappings: List[Tuple[int, int, int]] = [] # list of number-ranges (both inclusive) and offset between input and output

    def add_mapping(self, mapping: str) -> None:
        self.raw_mappings.append(([int(number) for number in mapping.split()]))

    def finalize(self) -> None:
        self.mappings = [(raw_mapping[1], raw_mapping[1]+raw_mapping[2]-1, raw_mapping[0]-raw_mapping[1]) for raw_mapping in self.raw_mappings]

    def perform_map(self, seed: int) -> int:
        for mapping in self.mappings:
            if seed >= mapping[0] and seed <= mapping[1]:
                return seed + mapping[2]
        return seed

    def __str__(self) -> str:
        return "Map=" + str([f"({mapping[0]}-{mapping[1]};offset={mapping[2]})" for mapping in self.mappings])
    
    def __repr__(self) -> str:
        return self.__str__()

def parse_seeds(seed_input: str):
    for seed_index in range(0, len(seed_input.split()[1:]), 2):
        for seed in range(int(seed_input.split()[1:][seed_index]), int(seed_input.split()[1:][seed_index]) + int(seed_input.split()[1:][seed_index+1])):
           yield seed


def parse_maps(inputOfDayWithoutSeeds: List[str]) -> List[Mapping]:
    maps: List[Mapping] = []
    curr_mapping = Mapping()
    for input_str in inputOfDayWithoutSeeds:
        if len(input_str) == 0:
            continue # do nothing on empty line
        elif input_str[0].isdigit():
            curr_mapping.add_mapping(input_str)
        elif len(input_str) > 0:
            curr_mapping.finalize()
            maps.append(curr_mapping)
            curr_mapping = Mapping()            
    curr_mapping.finalize()
    maps.append(curr_mapping)
    return maps

def solve(inputOfDay: str) -> str:
    amount_of_seeds: int = sum([int(seed_amount) for seed_amount in inputOfDay.splitlines()[0].split()[2::2]])
    amount_of_handled_seeds: int = 0
    print(f"I am going to check {amount_of_seeds} seeds.")
    seeds: List[int] = parse_seeds(inputOfDay.splitlines()[0])
    last_debug_percentage: int = 0
    maps: List[Mapping] = parse_maps(inputOfDay.splitlines()[3:])
    min_location: int = 987653129876541234987213651928375612983476 # a big number
    for seed in seeds:
        location: int = seed
        for mapping in maps:
            location = mapping.perform_map(location)
        amount_of_handled_seeds = amount_of_handled_seeds + 1
        if math.floor(amount_of_handled_seeds / amount_of_seeds) != last_debug_percentage:
            last_debug_percentage = last_debug_percentage + 1
            print(f"{last_debug_percentage}%")
        if location < min_location:
            min_location = location
            print(f"{datetime.now()} New nearest location: {min_location}")
    return str(min_location)

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
    with open('../input/day05-2.input', 'r') as f:
        inputOfDay = f.read()
    #test()
    print(solve(inputOfDay))
