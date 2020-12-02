using static System.Console;
using System.Linq;
using System.Collections.Generic;

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
            List<string> lines = FileUtils.ReadLines(fname);
            var total = lines.Where(IsValid).Count();
            WriteLine();
            WriteLine($"result: {total}");
        }

        private static bool IsValid(string line)
        {
            int min, max;
            char letter;
            string password;

            var parts = line.Split();
            password = parts[2];
            letter = parts[1][0];
            var interval = parts[0].Split('-');
            min = int.Parse(interval[0]);
            max = int.Parse(interval[1]);

            // WriteLine($"{min}, {max}, {letter}, {password}");

            var count = password.Where(c => c == letter).Count();

            return (count >= min) && (count <= max);
        }
    }
}
