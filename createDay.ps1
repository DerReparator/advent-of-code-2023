param(
    [Parameter(Mandatory)][int]$day
)

[string]$dayFolderName = 'day{0:d2}' -f $day

if ([System.IO.Directory]::Exists($dayFolderName))
{
    Write-Error "Folder $dayFolderName already exists."
    Exit 1
}

function Create-PythonSolutionContent {
    param (
        [int]$part
    )
    
return @"
# $dayFolderName; Part $part

import os
from typing import List, Tuple

def solve(inputOfDay: str) -> str:
    pass

def test():
    test_cases: List[Tuple[str, str]] = []
    test_dir: str = "../input_test"
    for test_case_input in [os.path.join(test_dir, fname) for fname in os.listdir(test_dir)]:
        if test_case_input.endswith("$part.input"):
            print(f"[DEBUG] Found test case input: {test_case_input}")
            test_case_expected = test_case_input.removesuffix("$part.input") + "$part.expected"
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
    with open('../input/$dayFolderName-$part.input', 'r') as f:
        inputOfDay = f.read()
    test()
    #print(solve(inputOfDay))
"@
}

$inputFolderName = "$dayFolderName/input"
$testFolderName = "$dayFolderName/input_test"
$pythonFolderName = "$dayFolderName/py"

New-Item -Path $dayFolderName -ItemType Directory
New-Item -Path $inputFolderName -ItemType Directory
New-Item -Path $testFolderName -ItemType Directory
New-Item -Path $pythonFolderName -ItemType Directory

# input
New-Item -Path "$inputFolderName/$dayFolderName-1.input"
New-Item -Path "$inputFolderName/$dayFolderName-2.input"

# tests
New-Item -Path "$testFolderName/testcase1.input"
New-Item -Path "$testFolderName/testcase1.expected"
New-Item -Path "$testFolderName/testcase2.input"
New-Item -Path "$testFolderName/testcase2.expected"

# python
Set-Content -Path "$pythonFolderName/solution1.py" -Value "$(Create-PythonSolutionContent(1))"
Set-Content -Path "$pythonFolderName/solution2.py" -Value "$(Create-PythonSolutionContent(2))"

Write-Host "Success!" -ForegroundColor Green
Set-Location $dayFolderName
