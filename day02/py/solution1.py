# day02; Part 1

import re
import os
from typing import List, Tuple, Dict

def parseCube(cube_record: str) -> Tuple[str,int]:
    splitted_record = cube_record.split(" ")
    return (splitted_record[1], int(splitted_record[0]))

def parseRound(round_record: str) -> Dict[str, int]:
    ret: Dict[str, int] = {}
    cubes_records = round_record.split(", ")
    for cube_record in cubes_records:
        parsed_cube = parseCube(cube_record)
        ret[parsed_cube[0]] = parsed_cube[1]
    return ret

def parseGame(game_record: str) -> List[Dict[str, int]]:
    parsed_game: List[Dict[str, int]] = []
    game_record = game_record.split(": ")[1] # strip "Game XYZ"
    round_records = game_record.split("; ")
    for round_record in round_records:
        parsed_round_record = parseRound(round_record)
        parsed_game.append(parsed_round_record)
    return parsed_game

THRESHOLD_RED = 12
THRESHOLD_GREEN = 13
THRESHOLD_BLUE = 14

def checkAmountOfCubes(round_record: Dict[str, int], color: str, amount: int) -> bool:
    if round_record.get(color, 0) > amount:
        return True # this is bad. max number of colors
    return False

def filterGames(games: List[List[Dict[str, int]]]) -> List[int]:
    ret: List[int] = []
    for i, game in enumerate(games, start=1):
        if any([checkAmountOfCubes(round_record, "red", THRESHOLD_RED) for round_record in game]):
            continue
        if any([checkAmountOfCubes(round_record, "blue", THRESHOLD_BLUE) for round_record in game]):
            continue
        if any([checkAmountOfCubes(round_record, "green", THRESHOLD_GREEN) for round_record in game]):
            continue
        ret.append(i)
    return ret

def solve(inputOfDay: str) -> str:
    parsed_games: List[List[Dict[str, int]]] = []
    for line in inputOfDay.splitlines():
        parsed_games.append(parseGame(line))
    filtered_game_ids = filterGames(parsed_games)
    print(f"Valid games: {filtered_game_ids}")
    return str(sum(filtered_game_ids))

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
    with open('../input/day02-1.input', 'r') as f:
        inputOfDay = f.read()
    #test()
    print(solve(inputOfDay))
