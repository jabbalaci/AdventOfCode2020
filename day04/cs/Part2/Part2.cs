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
            List<string> entries = ParseFile(fname);
            List<Passport> passports = entries.Select(s => new Passport(s)).ToList();
            var result = passports.Where(p => p.IsStrictlyValid()).Count();
            WriteLine(result);
        }

        private static List<string> ParseFile(string fname)
        {
            string content = FileUtils.Read(fname);
            // WriteLine("'" + content + "'");
            var entries = content.Split("\n\n")
                                 .Select(s => s.Replace("\n", " "))
                                 .ToList();
            return entries;
        }
    }
}
