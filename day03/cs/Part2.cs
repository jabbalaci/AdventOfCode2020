using static System.Console;
using System.Collections.Generic;

namespace AdventOfCode2020
{
    public class Part2
    {
        public static void Main(string[] args)
        {
            WriteLine("# Part 2");
            WriteLine("--------");
            WriteLine();
            // const string fname = "example.txt";
            const string fname = "input.txt";
            List<string> lines = FileUtils.ReadLines(fname);

            long a = CheckSlope(lines, 1, 1);
            long b = CheckSlope(lines, 3, 1);
            long c = CheckSlope(lines, 5, 1);
            long d = CheckSlope(lines, 7, 1);
            long e = CheckSlope(lines, 1, 2);

            // with type `int` I had an overflow error
            long result = a * b * c * d * e;
            WriteLine($"result: {result}");
        }

        private static long CheckSlope(List<string> lines, int right, int down)
        {
            long trees = 0;

            for (var i = 0; i < lines.Count; i += down)
            {
                var line = lines[i];
                // rotate <right> positions to the left (i / down) times
                // (i / down) shows how many times this loop is being executed
                for (var j = 0; j < (i / down); ++j)
                {
                    line = line[right..] + line[..right];
                }
                if (line[0] == '#') {
                    ++trees;
                }
            }

            return trees;
        }
    }
}
