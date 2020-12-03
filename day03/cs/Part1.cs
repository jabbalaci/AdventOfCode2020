using static System.Console;
using System.Collections.Generic;

/*
    This is not an optimal solution due to the high number
    of string operations. But this is what popped into my mind.

    As my dear friend Mocsa pointed out, it would have been better
    to use modulus operations.
*/

namespace AdventOfCode2020
{
    public class Part1
    {
        public static void Main(string[] args)
        {
            WriteLine("# Part 1");
            WriteLine("--------");
            WriteLine();
            // const string fname = "example.txt";
            const string fname = "input.txt";
            List<string> lines = FileUtils.ReadLines(fname);

            var trees = 0;
            for (var i = 0; i < lines.Count; ++i)
            {
                var line = lines[i];
                // rotate 3 positions to the left i times
                for (var j = 0; j < i; ++j)
                {
                    line = line[3..] + line[..3];
                }
                if (line[0] == '#') {
                    ++trees;
                }
            }
            WriteLine(trees);
        }
    }
}
