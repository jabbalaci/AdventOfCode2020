using static System.Console;
using System.Linq;

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

            var groups = FileUtils.Read(fname).Split("\n\n");
            var result = groups
                            .Select(s => s.Replace("\n", ""))
                            .Select(s => s.Distinct().Count())
                            .Sum();

            WriteLine(result);
        }
    }
}
