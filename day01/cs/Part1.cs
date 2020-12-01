using static System.Console;
using System.Linq;
using System.Collections.Generic;
using static AdventOfCode2020.Itertools;

namespace AdventOfCode2020
{
    public class Part1
    {
        public static void Main(string[] args)
        {
            WriteLine("# Part 1");
            WriteLine("--------");
            // const string fname = "example.txt";
            const string fname = "input.txt";
            const int GOAL = 2020;
            var numbers = FileUtils.ReadLinesAsInts(fname);
            // WriteLine(string.Join(", ", numbers));
            WriteLine();

            foreach (IEnumerable<int> iter in Combinations(numbers, 2))
            {
                var a = iter.ElementAt(0);
                var b = iter.ElementAt(1);

                if (a + b == GOAL)
                {
                    WriteLine($"# {a}, {b}");
                    WriteLine();
                    var result = a * b;
                    WriteLine($"result: {result}");

                    break;
                }
            }
        }
    }
}
