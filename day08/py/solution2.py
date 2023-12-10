# day08; Part 2

import os
from typing import List, Tuple, Dict

class Solver:
    def __init__(self, network: Dict[str, Tuple[str, str]], initial_node: str, movements: str) -> None:
        self.network = network
        self.movements = movements
        self.curr_node = initial_node
        self.curr_movement = 0

    def step(self) -> str:
        if (self.movements[self.curr_movement] == "L"):
            self.curr_node = self.network[self.curr_node][0]
        else:
            self.curr_node = self.network[self.curr_node][1]
        self.curr_movement = (self.curr_movement + 1) % len(self.movements)
        return self.curr_node[-1]

def parse_network(inputOfDay: str) -> Dict[str, Tuple[str, str]]:
    network: Dict[str, Tuple[str, str]] = {}
    for node_str in inputOfDay.splitlines()[2:]:
        network[node_str.split(" = ")[0]] = (node_str[7:10], node_str[12:15])
    return network

def solve(inputOfDay: str) -> str:
    movements = inputOfDay.splitlines()[0]
    network = parse_network(inputOfDay)
    solvers: List[Solver] = [Solver(network, initial_node, movements) for initial_node in network.keys() if initial_node.endswith('A')]
    no_of_steps: int = 0
    curr_solvers_state: str = "A" * len(solvers)
    while curr_solvers_state != "Z"*len(solvers):
        state_as_list = list(curr_solvers_state)
        for i, solver in enumerate(solvers):
            state_as_list[i] = solver.step()
        no_of_steps = no_of_steps + 1
        curr_solvers_state = ''.join(state_as_list)
        print(curr_solvers_state)
    return str(no_of_steps)

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
    with open('../input/day08-2.input', 'r') as f:
        inputOfDay = f.read()
    #test()
    print(solve(inputOfDay))
