using static System.Console;
using System.Linq;
using System.Collections.Generic;
using static AdventOfCode2020.Itertools;

namespace AdventOfCode2020
{
    public class Part2
    {
        public static void Main(string[] args)
        {
            WriteLine("# Part 2");
            WriteLine("--------");
            // const string fname = "example.txt";
            const string fname = "input.txt";
            const int GOAL = 2020;
            var numbers = FileUtils.ReadLinesAsInts(fname);
            // WriteLine(string.Join(", ", numbers));
            WriteLine();

            foreach (IEnumerable<int> iter in Combinations(numbers, 3))
            {
                var a = iter.ElementAt(0);
                var b = iter.ElementAt(1);
                var c = iter.ElementAt(2);

                if (a + b + c == GOAL)
                {
                    WriteLine($"# {a}, {b}, {c}");
                    WriteLine();
                    var result = a * b * c;
                    WriteLine($"result: {result}");

                    break;
                }
            }
        }
    }
}
