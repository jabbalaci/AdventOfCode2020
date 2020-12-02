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
            // const string fname = "example.txt";
            const string fname = "input.txt";
            List<string> lines = FileUtils.ReadLines(fname);
            var total = lines.Where(IsValid).Count();
            WriteLine();
            WriteLine($"result: {total}");
        }

        private static bool IsValid(string line)
        {
            int pos1, pos2;
            int idx1, idx2;
            char letter;
            string password;

            var parts = line.Split();
            password = parts[2];
            letter = parts[1][0];
            var interval = parts[0].Split('-');
            pos1 = int.Parse(interval[0]);
            pos2 = int.Parse(interval[1]);
            idx1 = pos1 - 1;
            idx2 = pos2 - 1;

            // WriteLine($"{idx1}, {idx2}, {letter}, {password}");

            var count = 0;
            if (password[idx1] == letter) ++count;
            if (password[idx2] == letter) ++count;

            return count == 1;
        }
    }
}
