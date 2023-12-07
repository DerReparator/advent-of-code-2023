Console.WriteLine("Advent of Code 2023 - Day 05 - Part 2");

#if DEBUG
    const string inputFile = "../../../../../input_test/testcase2.input";
    const long expected = 46;
#else
    const string inputFile = "../../../../../input/day05-2.input";
#endif // DEBUG

List<string> inputOfDay = new List<string>(File.ReadLines(inputFile));

class Mapping
{
    private List<Tuple<int, int, int>> _rawMappings = new List<Tuple<int, int, int>>();
    
    /// list of number-ranges (both inclusive) and offset between input and output    
    List<Tuple<int, int, int>> Mappings { get; } = new();

    void addMapping(string mapping)
    {
        _rawMappings.Add(mapping
            .Split()
            .Select(s => int.Parse(s))
            .ToArray()
            .(arr => new Tuple<int, int, int>(arr[0], arr[1], arr[2])));
    }

    void finalize()
    {

    }

    long performMap(long seed)
    {

    }
}

IEnumerable<long> parseSeeds(string seedInput)
{
    var seedStrings = seedInput.Split().Skip(1).ToList();
    foreach (int seedIndex in Enumerable.Range(0, seedStrings.Count).Where((elem, idx) => idx % 2 == 0))
    {
        foreach (long seed in Enumerable.Range(
            int.Parse(seedStrings[seedIndex]),
            int.Parse(seedStrings[seedIndex+1])
            ))
        {
            yield return seed;
        }
    }
}

long solve(List<string> inputOfDay)
{
    long minLocation = 226439822; // already found during Python testing
    IEnumerable<long> seeds = parseSeeds(inputOfDay[0]);
#if DEBUG
    Console.WriteLine(string.Join(";", seeds));
#endif
    return 0;
}

long result = solve(inputOfDay);

#if DEBUG
    string resultState = result == expected ? "SUCCESS" : "FAIL";
    Console.WriteLine($"{resultState}: Expected = {expected}; Actual = {result}");
#else
    Console.WriteLine($"Result: {result}");
#endif
