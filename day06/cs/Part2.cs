using static System.Console;
using System.Linq;
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

            var groups = FileUtils.Read(fname).Split("\n\n");

            var total = 0;
            foreach (var group in groups)
            {
                var elems = group.Split("\n");
                IEnumerable<char> common = elems[0];
                foreach (var elem in elems)
                {
                    common = common.Intersect(elem);
                }
                total += common.Count();
            }
            WriteLine(total);
        }
    }
}
